from transformers import AutoTokenizer, BitsAndBytesConfig
import numpy as np
import requests
from PIL import Image
from io import BytesIO

class Llava:
    """
    Модель для генерации текста по изображению
    """

    def __init__(self) -> None:
        self.model_path = "4bit/llava-v1.5-13b-3GB"
        self.__load_model__()

    def __load_model__(self) -> None:
        try:
            print('Loading Llava')

            print('Loaded Llava')

        except Exception as e:
            print(e)

    def get_image(self, img_path: str) -> np.array:
        """
        Считывание изображения по ссылке или локально
        """

        if img_path.startswith('http') or img_path.startswith('https'):
            response = requests.get(img_path)
            image = Image.open(BytesIO(response.content)).convert('RGB')
        else:
            image = Image.open(img_path).convert('RGB')
        return image

    def caption_image(self, img_path: str) -> str:
        """
        Генерация описания по изображению
        """
        image = self.get_image(img_path)
        print(f'Generating text')
        return image


