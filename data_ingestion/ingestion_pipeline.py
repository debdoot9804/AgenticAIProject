import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader,Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
from utils.model_loader import ModelLoader
from utils.config_loader import load_config
from pinecone import ServerlessSpec, Pinecone
from uuid import uuid4
import sys
from exception.exception import TradingException
load_dotenv()


class DataIngestion:
    def __init__(self):
        print("Initializing data ingestion pipeline")
        self.config=load_config()
        self.model_loader=ModelLoader()
        self.load_env_variables()

    def load_env_variables(self):
         """For validating env variables"""

        required=["GOOGLE_API_KEY","GROQ_API_KEY","PINECONE_API_KEY"]
        missing=[i for i in required if not os.getenv(i)] 
        if missing:
            raise EnvironmentError(f"Missing env variables"{missing})

    def load_doc(self,files)-> List[Document]:
        """Loading documents"""
        try:
            docs=[]
            for i in files:
                file_extension=os.path.splitext(i.filename)[1].lower()
                suffix=file_extension if file-extension in [".pdf",".docx"] else ".tmp"
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                    temp_file.write(uploaded_file.file.read())
                    temp_path = temp_file.name

                if file_extension == ".pdf":
                    loader = PyPDFLoader(temp_path)
                    docs.extend(loader.load())
                elif file_extension == ".docx":
                    loader = Docx2txtLoader(temp_path)
                    docs.extend(loader.load())
                else:
                    print(f"Unsupported file type: {uploaded_file.filename}")
            return documents
        
        except Exception as e:
            raise TradingException(e, sys)

    
    def store_in_vectordb(self,docs:List[Document]):
        """For storing data in vector db"""
        try:
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=800,
                chunk_overlap=200,
                length_function=len
            )

            docs=text_splitter.split_documents(docs)

            pc=Pinecone(api_key=self.PINECONE_API_KEY)
            index_name = self.config["vector_db"]["index_name"]

            pc.create_index(
                    name=index_name,
                    dimension=768,  # adjust if needed based on embedding model
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
                )
            
            index=pc.Index(index_name)
            vector_store=PineconeVectorStore(index=index,embedding=self.model_loader.load_embedding())
            uuids = [str(uuid4()) for _ in range(len(documents))]

            vector_store.add_documents(documents=docs, ids=uuids)

        except Exception as e:
            raise TradingException(e,sys)
        

    def run_pipeline(self,files):
        try:
            documents=self.load_doc(files)
            if not documents:
                print("No documents found")
                return ""
                
            self.store_in_vectordb(documents)
        except Exception as e:
            raise TradingException(e,sys)
        
if __name__=="__main__":
    pass


        



        
