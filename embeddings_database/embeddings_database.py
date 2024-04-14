import os
import faiss
import numpy as np


class EmbeddingsDatabase:
	EMBEDDINGS_DATABASE_PATH = "embeddings_database/embeddings_database_idmap.index"

	def __init__(self, emb_size: int):
		if os.path.exists(self.EMBEDDINGS_DATABASE_PATH):
			self.index_idmap = faiss.read_index(self.EMBEDDINGS_DATABASE_PATH)
		else:
			self.index = faiss.IndexFlatL2(emb_size)
			self.index_idmap = faiss.IndexIDMap(self.index)

	def add_embedding(self, img_emb, img_ind):
		self.index_idmap.add_with_ids(img_emb, img_ind)

	def find_similar(self, query_emb, k: int):
		_, indices = self.index_idmap.search(query_emb, k)
		return indices[0].tolist()

	def save_database(self):
		faiss.write_index(self.index_idmap, self.EMBEDDINGS_DATABASE_PATH)
