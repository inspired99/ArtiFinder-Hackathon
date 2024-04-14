from ml_framework.clip.clip import CLIP
from ml_framework.swin.swin import Swin
from ml_framework.llava.llava import Llava

# Remove warnings
import warnings
warnings.filterwarnings("ignore")


class MLFramework:
	def __init__(self):
		self.clip = CLIP()
		self.swin = Swin(is_train=False)
		self.llava = Llava()

	def get_img_embedding(self, img_path: str):
		return self.clip.get_img_embedding(img_path)

	def get_img_class(self, img_path: str):
		return self.swin.get_img_class(img_path)

	def get_img_description(self, img_path: str):
		return self.llava.caption_image(img_path)

	def get_emb_size(self) -> int:
		return self.clip.get_emb_size()


def test_ml():
	img_path = "exhibits_database/images/20110231.jpg"

	ml_framework = MLFramework()

	print(ml_framework.get_emb_size())
	print(ml_framework.get_img_class(img_path))
	print(ml_framework.get_img_embedding(img_path))
	print(ml_framework.get_img_description(img_path))


if __name__ == "__main__":
	test_ml()
