import os
import torch
import pandas as pd
from PIL import Image
import torch.nn as nn
from torchvision import transforms
from torchvision.models import resnet101
from pytorch_lightning import LightningModule, Trainer
from pytorch_lightning.callbacks import EarlyStopping
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
from torchmetrics import Accuracy


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


class ResNet(LightningModule):
	WEIGHTS_PATH = "resnet.pt"

	TRAIN_TRANSFORM = transforms.Compose([
		transforms.Resize(256),
		transforms.RandomCrop(224),
		transforms.RandomHorizontalFlip(p=0.5),
		transforms.ToTensor(),
		transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
	])

	INFERENCE_TRANSFORM = transforms.Compose([
		transforms.Resize(256),
		transforms.CenterCrop(224),
		transforms.ToTensor(),
		transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
	])

	def __init__(self, is_train):
		super().__init__()

		self.model = resnet101(pretrained=is_train)
		self.model.fc = nn.Linear(2048, 15)

		if is_train:
			for param in self.model.parameters():
				param.requires_grad = False

			for param in self.model.fc.parameters():
				param.requires_grad = True

			self.loss = nn.CrossEntropyLoss()
			self.calculate_accuracy = Accuracy(task="multiclass", num_classes=15)

			self.loss_outputs = {'train': [], 'val': []}
			self.acc_outputs = {'train': [], 'val': []}

		else:
			self.gpu_device = torch.device("cuda")

			# self.model.load_state_dict(torch.load(self.WEIGHTS_PATH, map_location=self.gpu_device))
			self.model.eval()
			self.model.to(self.gpu_device)

	def configure_optimizers(self):
		optimizer = torch.optim.Adam(self.parameters(), lr=1e-4, weight_decay=1e-6)
		return optimizer

	def step(self, batch, mode):
		x, y = batch
		logits = self.model.forward(x)
		loss = self.loss(logits, y)

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
	train_dataset = ImagesDataset(train_img_names, train_img_group, ResNet.TRAIN_TRANSFORM)
	val_dataset = ImagesDataset(val_img_names, val_img_group, ResNet.INFERENCE_TRANSFORM)

	# Create dataloaders
	train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=2)
	val_dataloader = DataLoader(val_dataset, batch_size=16, shuffle=False, num_workers=2)

	# Create model
	model = ResNet(is_train=True)

	early_stopping_callback = EarlyStopping(
		monitor='acc',
		patience=3,
		mode='max'
	)

	# Create trainer
	trainer = Trainer(
		max_epochs=10,
		accelerator="gpu",
		callbacks=[early_stopping_callback]
	)

	# Train
	trainer.fit(model, train_dataloader, val_dataloader)

	# Save weights
	model.save_weights(ResNet.WEIGHTS_PATH)


if __name__ == "__main__":
	DATASET_PATH = '/kaggle/input/hackcp'
	train_classification_model(DATASET_PATH)
