from chromadb import PersistentClient
from chromadb.config import Settings
import numpy as np
from sentence_transformers import SentenceTransformer
import logging
from utils import read_text_from_file

logger = logging.getLogger(__name__)

class Query():

	def __init__(self):
		"""Initialize embedder, Chroma client, and collection"""
	
		logging.info("instantiating embedding and chromadb...")

		# 1. Embedder
		self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
		
		# 2. Chroma persistent client
		self.chroma = PersistentClient(		
			path="../data/chroma"
		)

		# 3. Collection
		self.collection = self.chroma.get_or_create_collection(
			name="cv_stuff",
			embedding_function=None
		)

		# 4. Precompute embedding
		job_description = read_text_from_file(path="../data/job_description.txt")

		self.query_embedding = self.embedder.encode(job_description)


			
	def query(self, metadata: str):
		"""fetches documents from chromaDB.

		Queries a ChromaDB collection based on given metadata

		Args:
			metadata: metadata information

		Returns:
			A List of Documents corresponding to the metadata. For example:

			["Document 1", "Document 2", "Document 3", "..."]
		"""

	
		results = self.collection.query(
			query_embeddings=[self.query_embedding],
			where={"type": metadata},
			n_results=3
		)

		return results["documents"]
