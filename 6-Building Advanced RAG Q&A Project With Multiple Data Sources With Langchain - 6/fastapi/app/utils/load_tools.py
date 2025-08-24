
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain.tools.retriever import create_retriever_tool
from app.dependencies import retriever

# Wikipedia Tool
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Arxiv Tool
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)

# LangSmith Retriever Tool
langsmith_tool = create_retriever_tool(
    retriever, "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!"
)

# List of Tools
TOOLS = [wiki_tool, arxiv_tool, langsmith_tool]
