import faiss
import asyncio
from concurrent.futures import ProcessPoolExecutor
import numpy as np


class EmbeddingsDatabase:
	def __init__(self, executor: ProcessPoolExecutor, emb_size: int):
		self.executor = executor
		self.index = faiss.IndexFlatL2(emb_size)

	def add_embedding(self, new_emb):
		self.index.add(1, new_emb)
		self.index.add_with_ids()

	def find_similar(self, query_emb, k: int):
		distances, indices = self.index.search(query_emb, k)
