from setuptools import find_packages,setup

setup(name="Agentic trading system",
version="1.0.0",
packages=find_packages(),
install_requires=['lancedb',
'langchain',
'langgraph',
'langchain_core'
'tavily_python',
'polygon'
'numpy'
'pandas'
'langchain_groq']
)