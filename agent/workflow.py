from langgraph.graph import StateGraph,START
from langgraph.graph.message import add_messages
from langgraph.prebuilt.tool_node import Toolnode,tools_condition
from langchain_core.messages import AIMessage,HumanMessage
from typing_extensions import Annotated,TypedDict
from utils.model_loaders import ModelLoader
from toolkit.tools import tool


class State(TypeDict):
    messages: Annotated[list,add_messages]


class GraphBuilder:
    def __init__(self):
        


    def chat_model(self,state:State):

        pass

    def build():
        pass

    def get_graph():
        pass