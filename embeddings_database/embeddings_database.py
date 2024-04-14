import faiss
import numpy as np


class EmbeddingsDatabase:
	def __init__(self, emb_size: int):
		self.index = faiss.IndexFlatL2(emb_size)
		self.index_idmap = faiss.IndexIDMap(self.index)

	def add_embedding(self, img_emb, img_ind):
		self.index_idmap.add_with_ids(img_emb, img_ind)

	def find_similar(self, query_emb, k: int):
		_, indices = self.index_idmap.search(query_emb, k)
		return indices
