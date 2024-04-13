from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from numpy.linalg import norm

import torch
import numpy as np


class CLIP:
	def __init__(self):
		self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
		self.model_path = 'openai/clip-vit-base-patch32'
		self.model = None
		self.processor = None
		self.__load_model__()

	def __load_model__(self) -> None:
		"""
		Инициализация модели
		"""
		self.processor = CLIPProcessor.from_pretrained(self.model_path)
		self.model = CLIPModel.from_pretrained(self.model_path)
		self.model.to(self.device)
		print(f'Loaded CLIP')

	@staticmethod
	def normalize_emb(emb):
		emb = emb.detach().cpu().numpy()
		if len(emb.shape) == 1:
			norm_factor = np.linalg.norm(emb)
			emb = emb / norm_factor
		else:
			norm_factor = np.linalg.norm(emb, axis=1)
			emb = (emb.T / norm_factor).T
		return emb

	@staticmethod
	def cosine_sim(emb_1, emb_2) -> float:
		"""
		Косинусная близость между векторами
		"""

		cos_sim = np.dot(emb_1, emb_2.T) / (
				norm(emb_1, axis=1) * norm(emb_2, axis=1)
		)
		cos_sim = cos_sim.reshape(-1)[0]
		return cos_sim

	def get_text_emb(self, text: str):
		"""
		Извлечение эмбеддинга по тексту
		"""
		tokens = self.processor(
			text=text,
			padding=True,
			images=None,

			return_tensors='pt'
		).to(self.device)
		tokens.keys()

		text_emb = self.model.get_text_features(**tokens)
		text_emb = self.normalize_emb(text_emb)
		return text_emb

	def get_img_embedding(self, img_path: str):
		"""
		Получение эмбеддинга по изображению размера 1 х 512
		"""

		image = Image.open(img_path).convert('RGB')
		images = self.processor(
			text=None,
			images=image,
			return_tensors='pt'
		)['pixel_values'].to(self.device)
		emb = self.model.get_image_features(images)
		emb = self.normalize_emb(emb)
		return emb

	def get_emb_size(self) -> int:
		return self.model.config.projection_dim
