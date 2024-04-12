import torch
from PIL import Image
from torchvision import transforms
import lightning as L


class ResNet(L.LightningModule):
	def __init__(self):
		super().__init__()

		self.model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet101', pretrained=True)
		self.model.eval()

		# self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
		#
		# if torch.cuda.is_available():
		# 	self.model.to('cuda')

	@staticmethod
	def preprocess(self, img: Image):
		preprocess = transforms.Compose([
			transforms.Resize(256),
			transforms.CenterCrop(224),
			transforms.ToTensor(),
			transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
		])
		input_tensor = preprocess(img)
		input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

		return input_batch

	def get_img_class(self, img_path):
		img = Image.open(img_path)
		input_batch = self.preprocess(img)
		with torch.no_grad():
			output = self.model(input_batch)

		# Tensor of shape 1000, with confidence scores over ImageNet's 1000 classes
		print(output[0])
		# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
		probabilities = torch.nn.functional.softmax(output[0], dim=0)
		print(probabilities)

	def training_step(self, batch, batch_idx):
		# training_step defines the train loop.
		# it is independent of forward
		x, y = batch
		x = x.view(x.size(0), -1)
		z = self.encoder(x)
		x_hat = self.decoder(z)
		loss = nn.functional.mse_loss(x_hat, x)
		# Logging to TensorBoard (if installed) by default
		self.log("train_loss", loss)
		return loss

	def configure_optimizers(self):
		optimizer = optim.Adam(self.parameters(), lr=1e-3)
		return optimizer
