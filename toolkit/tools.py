from langchain.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from lancedb.rerankers import LinearCombinationReranker
from langchain_community.vectorstores import LanceDB
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults
from data_models.models import RagToolSchema


@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """retriever tool"""
    return ""

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




    

