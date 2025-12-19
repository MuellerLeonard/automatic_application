from chromadb import PersistentClient
from chromadb.config import Settings
import numpy as np
from sentence_transformers import SentenceTransformer
import logging
import json

logger = logging.getLogger(__name__)

class Insert():

	def __init__(self):

		logging.info("instantiating embedding and chromadb...")
		
		# 1. Embedder
		self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
	
		# 2. Chroma persistent client	
		self.chroma = PersistentClient(path="../data/chroma")
	
		# 3. Collection	
		self.collection = self.chroma.get_or_create_collection(
			name="cv_stuff",
			embedding_function=None
		)
					
	def insert(self):
	
		self.add(metadata="projects")

		self.add(metadata="beginning")

		self.add(metadata="tech_skills")

		self.add(metadata="soft_skills")

		self.add(metadata="ending")
	
	def add(self, metadata):
			
		# Insert Text file here:
		logging.info("reading documents from file...")
		
		ids = []
		documents = []
		metadatas = {"type": metadata}
		
		with open("../data/documents.json", "r") as f:
			config = json.load(f)

		for item in config[metadata]: 
			key = list(item.keys())[0]
			value = list(item.values())[0]	

			ids.append(key)
			documents.append(value)

		embeddings = []

		metadatas = [metadatas] * len(documents)		

		logging.info("embedding the documents...")	

		embeddings = self.embedder.encode(documents)
		
		# Add to collection

		logging.info("adding the documents, embeddings and ids to the collection...")
		# print(f"Docs: {documents} Embeddings: {embeddings} IDS: {ids} metadatas: {metadata}")
	
		self.collection.add(
			documents=documents,
			embeddings=embeddings,
			ids=ids,
			metadatas=metadatas
		)	
