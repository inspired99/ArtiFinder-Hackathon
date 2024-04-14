import os
import torch
import pandas as pd
from PIL import Image
from torch import nn
from torchvision import transforms as T
from pytorch_lightning import LightningModule, Trainer
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
from torchmetrics import Accuracy
import timm
from timm.loss import LabelSmoothingCrossEntropy


CATEGORY_TO_LABEL = {
	'Минералогия': 0, 'Археология': 1, 'Нумизматика': 2, 'Печатная продукция': 3, 'Графика': 4,
	'Фото, негативы': 5, 'ДПИ': 6, 'Естественнонауч.коллекция': 7, 'Скульптура': 8, 'Прочие': 9,
	'Редкие книги': 10, 'Техника': 11, 'Оружие': 12, 'Документы': 13, 'Живопись': 14
}

LABEL_TO_CATEGORY = {
	0: 'Минералогия', 1: 'Археология', 2: 'Нумизматика', 3: 'Печатная продукция', 4: 'Графика',
	5: 'Фото, негативы', 6: 'ДПИ', 7: 'Естественнонауч.коллекция', 8: 'Скульптура', 9: 'Прочие',
	10: 'Редкие книги', 11: 'Техника', 12: 'Оружие', 13: 'Документы', 14: 'Живопись'
}


def image_preprocessing(img_path, img_transform):
	img = Image.open(img_path)
	img = img.convert("RGB")  # Convert to RGB (dataset contains gray-scale and images with alpha channel)
	transformed_img = img_transform(img)
	return transformed_img


class ImagesDataset(Dataset):
	def __init__(self, imgs_paths, imgs_categories, img_transform):
		self.imgs_paths = imgs_paths
		self.imgs_categories = imgs_categories
		self.img_transform = img_transform

	def __len__(self):
		return len(self.imgs_paths)

	def __getitem__(self, idx):
		img_path = self.imgs_paths.iloc[idx]
		transformed_img = image_preprocessing(img_path, self.img_transform)

		category = self.imgs_categories.iloc[idx]
		label = CATEGORY_TO_LABEL[category]

		return transformed_img, label


class Swin(LightningModule):
	WEIGHTS_PATH = "swin.pt"

	TRAIN_TRANSFORM = T.Compose([
		T.RandomHorizontalFlip(),
		T.RandomVerticalFlip(),
		T.RandomApply(torch.nn.ModuleList([T.ColorJitter()]), p=0.25),
		T.Resize(256),
		T.CenterCrop(224),
		T.ToTensor(),
		T.Normalize(timm.data.IMAGENET_DEFAULT_MEAN, timm.data.IMAGENET_DEFAULT_STD),
		T.RandomErasing(p=0.1, value='random')
	])

	INFERENCE_TRANSFORM = T.Compose([
		T.Resize(256),
		T.CenterCrop(224),
		T.ToTensor(),
		T.Normalize(timm.data.IMAGENET_DEFAULT_MEAN, timm.data.IMAGENET_DEFAULT_STD),
	])

	def __init__(self, is_train):
		super().__init__()

		hub_url = "SharanSMenon/swin-transformer-hub:main"
		model_name = "swin_tiny_patch4_window7_224"
		self.model = torch.hub.load(hub_url, model_name, pretrained=is_train)

		n_inputs = self.model.head.in_features
		self.model.head = nn.Sequential(
			nn.Linear(n_inputs, 512),
			nn.ReLU(),
			nn.Dropout(0.3),
			nn.Linear(512, len(CATEGORY_TO_LABEL))
		)

		if is_train:
			for param in self.model.parameters():
				param.requires_grad = False

			for param in self.model.head.parameters():
				param.requires_grad = True

			self.criterion = LabelSmoothingCrossEntropy()
			self.calculate_accuracy = Accuracy(task="multiclass", num_classes=15)

			self.loss_outputs = {'train': [], 'val': []}
			self.acc_outputs = {'train': [], 'val': []}

		else:
			self.gpu_device = torch.device("cuda")

			self.model.load_state_dict(torch.load(self.WEIGHTS_PATH, map_location=self.gpu_device))
			self.model.eval()
			self.model.to(self.gpu_device)

	def configure_optimizers(self):
		optimizer = torch.optim.AdamW(self.model.parameters(), lr=0.001, weight_decay=1e-4)
		lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.99)

		lr_dict = {
			"scheduler": lr_scheduler,
			"monitor": "loss"
		}

		return [optimizer], [lr_dict]

	def step(self, batch, mode):
		x, y = batch
		logits = self.model.forward(x)
		loss = self.criterion(logits, y)

		# Show loss on step
		self.log("loss", loss, on_step=True, on_epoch=True, prog_bar=True)

		# Show accuracy on step
		y_preds = torch.argmax(logits, dim=1)
		acc = self.calculate_accuracy(y_preds, y)
		self.log("acc", acc, on_step=True, on_epoch=True, prog_bar=True)

		self.loss_outputs[mode].append(loss)
		self.acc_outputs[mode].append(acc)

		return {'loss': loss, "acc": acc}

	def training_step(self, batch, batch_idx):
		return self.step(batch, 'train')

	def validation_step(self, batch, batch_idx, dataloader_idx=0):
		return self.step(batch, 'val')

	def on_epoch_end(self, mode):
		avg_loss = torch.stack(self.loss_outputs[mode]).mean()
		avg_acc = torch.stack(self.acc_outputs[mode]).mean()

		print(f"\n{mode}: loss = {avg_loss:.2f}, accuracy = {avg_acc:.3f}")

		self.loss_outputs[mode].clear()
		self.acc_outputs[mode].clear()

	def on_train_epoch_end(self):
		self.on_epoch_end("train")

	def on_validation_epoch_end(self):
		self.on_epoch_end("val")

	def save_weights(self, path):
		torch.save(self.model.state_dict(), path)

	def get_img_class(self, img_path):
		transformed_img = image_preprocessing(img_path, self.INFERENCE_TRANSFORM)
		transformed_img = transformed_img.unsqueeze(0)  # Batch dim
		transformed_img = transformed_img.to(self.gpu_device)

		with torch.inference_mode():
			logits = self.model.forward(transformed_img)

		y_preds = torch.argmax(logits, dim=1)[0]

		return y_preds.item()


def train_classification_model(dataset_path):
	dataset_img_path = dataset_path + '/' + 'train'

	data = pd.read_csv(dataset_path + '/' + 'train.csv', sep=';')

	data['object_id'] = data['object_id'].astype(str)
	data['img_path'] = dataset_img_path + '/' + data['object_id'] + '/' + data['img_name']

	train_img_names, val_img_names, train_img_group, val_img_group = train_test_split(
		data['img_path'], data['group'], test_size=0.33, random_state=42
	)

	# Create datasets
	train_dataset = ImagesDataset(train_img_names, train_img_group, Swin.TRAIN_TRANSFORM)
	val_dataset = ImagesDataset(val_img_names, val_img_group, Swin.INFERENCE_TRANSFORM)

	# Create dataloaders
	train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=4)
	val_dataloader = DataLoader(val_dataset, batch_size=16, shuffle=False, num_workers=4)

	# Create model
	model = Swin(is_train=True)

	# Create trainer
	trainer = Trainer(
		max_epochs=2,
		accelerator="gpu"
	)

	# Train
	trainer.fit(model, train_dataloader, val_dataloader)

	# Save weights
	model.save_weights(Swin.WEIGHTS_PATH)


if __name__ == "__main__":
	DATASET_PATH = '/kaggle/input/hackcp'
	train_classification_model(DATASET_PATH)
