import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.config_loader import load_config

load_dotenv()

class ModelLoader:
    """for loading llm and embedding models"""

    def __init__(self):
        self.config=load_config()
        self.validate_env_variables()

    def validate_env_variables(self):
        """For validating env variables"""

        required=["GOOGLE_API_KEY","GROQ_API_KEY"]
        missing=[i for i in required if not os.getenv(i)] 
        if missing:
            raise EnvironmentError(f"Missing env variables"{missing})
        
    def load_embedding(self):
        """Loading embedding model"""
        print("loading embedding model")
        embed_model=self.config["embedding_model"]["model_name"]
        return GoogleGenerativeAIEmbeddings(model=embed_model)
    def load_llm(self):
        """Load LLM model"""

        print("Loading LLM") 
        llm_model=self.config["llm"]["groq"]["model_name"]
        groq_model=ChatGroq(model=llm_model) 
        return groq_model

        



