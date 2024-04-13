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

	async def get_img_embedding(self, img_path: str):
		result = await asyncio.get_running_loop().run_in_executor(
			self.executor, self.clip.get_img_embedding, img_path
		)
		return result

	async def get_img_class(self, img_path: str):
		result = await asyncio.get_running_loop().run_in_executor(
			self.executor, self.resnet.get_img_class, img_path
		)
		return result

	async def get_img_description(self, img_path: str):
		result = await asyncio.get_running_loop().run_in_executor(
			self.executor, self.llava.caption_image, img_path
		)
		return result

	def get_emb_size(self) -> int:
		return self.clip.get_emb_size()


async def test_ml():
	img_path = "~/ArtiFinder/exhibits_database/images/20110231.jpg"

	with ProcessPoolExecutor(max_workers=1) as ml_executor:
		ml_framework = MLFramework(ml_executor)

		print(ml_framework.get_emb_size())
		print(await ml_framework.get_img_class(img_path))
		print(await ml_framework.get_img_embedding(img_path))
		print(await ml_framework.get_img_description(img_path))


if __name__ == "__main__":
	asyncio.run(test_ml())
