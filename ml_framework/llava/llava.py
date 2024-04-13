from transformers import AutoTokenizer, BitsAndBytesConfig
from PIL import Image
from io import BytesIO
import numpy as np
import requests
import torch

from ml_framework.llava.llava_model import LlavaMetaForCausalLM, LlavaLlamaForCausalLM


class Llava:
    """
    Модель для генерации текста по изображению
    """

    def __init__(self) -> None:
        self.model_path = "4bit/llava-v1.5-13b-3GB"
        self.__load_model__()
        self.model = None
        self.tokenizer = None
        self.image_processor = None

    def __load_model__(self) -> None:
        try:
            print('Loading Llava')

            kwargs = {"device_map": "auto", "load_in_4bit": True,
                      'quantization_config': BitsAndBytesConfig(
                          load_in_4bit=True,
                          bnb_4bit_compute_dtype=torch.float16,
                          bnb_4bit_use_double_quant=True,
                          bnb_4bit_quant_type='nf4'
                      )}
            self.model = LlavaLlamaForCausalLM.from_pretrained(self.model_path, low_cpu_mem_usage=True, **kwargs)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False)

            vision_tower = self.model.get_vision_tower()
            if not vision_tower.is_loaded:
                vision_tower.load_model()
            vision_tower.to(device='cuda')
            self.image_processor = vision_tower.image_processor

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
