from langchain.tools import tool
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults
from data_models.models import RagToolSchema
from dotenv import load_dotenv
import os
from utils.config_loader import load_config
from models.model_loader import ModelLoader


load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
polygon_api_wrapper=PolygonAPIWrapper()
model_loader=ModelLoader()
config=load_config()


@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """retriever tool"""
    pc=Pinecone(api_key=PINECONE_API_KEY)
    vector_store=PineconeVectorStore(index=pc.Index(config["vector_db"]["index_name"]),embedding=model_loader.load_embedding())
    
    

@tool
def tavily_tool(question:str):
    """Tavily tool"""
    return TavilySearchResults(question,
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True

    )

@tool
def polygon_tool():
    """Polygon tool"""
    return PolygonFinancials(api_wrapper=PolygonAPIWrapper)

@tool
def bing_tool():
    """Bing tool"""
    return BindSearchResults()


def get_all_tool(question):
    return[
        retriever_tool(question),
        tavily_tool,
        polygon_tool,
        bing_tool
    ]

if __name__=='__main__':
    print(get_all_tool("I am question"))




    

