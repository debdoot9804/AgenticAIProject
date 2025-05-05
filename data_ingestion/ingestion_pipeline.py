import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader,Doc2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone



class DataIngestion:
    def __init__(self):
        pass

    def load_env_variables(self):
        pass

    def load_doc(self):
        pass

    def store in vectordb(self):
        pass
