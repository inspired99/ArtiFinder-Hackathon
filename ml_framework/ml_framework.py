from ml_framework.clip.clip import CLIP
from ml_framework.resnet.resnet import ResNet
from ml_framework.llava.llava import Llava

import asyncio
from concurrent.futures import ProcessPoolExecutor


class MLFramework:
	def __init__(self, executor: ProcessPoolExecutor):
		self.clip = CLIP()
		self.resnet = ResNet(is_train=False)
		self.llava = Llava()
		self.executor = executor

	async def get_img_embedding(self, img):
		result = await asyncio.get_running_loop().run_in_executor(
			self.executor, self.clip.get_img_embedding, img
		)
		return result

	async def get_img_class(self, img):
		result = await asyncio.get_running_loop().run_in_executor(
			self.executor, self.resnet.get_img_class, img
		)
		return result

	async def get_img_description(self, img):
		result = await asyncio.get_running_loop().run_in_executor(
			self.executor, self.llava.caption_image, img
		)
		return result

	def get_emb_size(self) -> int:
		return self.clip.get_emb_size()
