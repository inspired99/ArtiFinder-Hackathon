from time import time
from transformers import AutoTokenizer, BitsAndBytesConfig
from PIL import Image
from io import BytesIO
from ml_framework.llava.llava_model import LlavaLlamaForCausalLM
from ml_framework.llava.llava_utils import disable_torch_init, tokenizer_image_token, get_model_name_from_path
from ml_framework.llava.llava_model import IMAGE_TOKEN_INDEX

import numpy as np
import requests
import torch
import bitsandbytes

class Llava:
    """
    Модель для генерации текста по изображению
    """

    def __init__(self) -> None:
        self.model_path = "4bit/llava-v1.5-13b-3GB"
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.__load_model__()
        self.model = None
        self.tokenizer = None
        self.image_processor = None

    def __load_model__(self) -> None:
        """
        Инициализация модели
        """

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

    def get_image(self, img_path: str):
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
        start = time()
        if img_path.startswith('http') or img_path.startswith('https'):
            response = requests.get(img_path)
            image = Image.open(BytesIO(response.content)).convert('RGB')
        else:
            image = Image.open(img_path).convert('RGB')
        disable_torch_init()
        image_tensor = self.image_processor.preprocess(image, return_tensors='pt')['pixel_values'].half().cuda()
        raw_prompt = 'Беседа между любопытным человеком и помощником искусственного интеллекта. Помощник дает полезные, подробные и вежливые ответы на вопросы человека. Давай ответы на русском языке. Answer in russian language. ###Человек: <im_start><image><im_end>. Человек: Опиши изображение в деталях###Ассистент:'
        input_ids = tokenizer_image_token(raw_prompt, self.tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(
            0).cuda()
        with torch.inference_mode():
            output_ids = self.model.generate(input_ids, images=image_tensor, do_sample=True, temperature=0.2,
                                        max_new_tokens=1024, use_cache=True)
        outputs = self.tokenizer.decode(output_ids[0, input_ids.shape[1]:]).strip()
        output = outputs.rsplit('</s>', 1)[0]
        end = time()
        print(f'#####_____ time : {end - start}')
        return output
