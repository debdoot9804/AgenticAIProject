from setuptools import find_packages,setup

setup(name="agentic-trading-system",
       version="1.0.0",
       author="Debdoot",
       packages=find_packages(),
       install_requires=['lancedb','langchain','langgraph','tavily-python','polygon']
       )