# tools/tavily_search.py

from langchain.tools import tool
from tavily import TavilyClient
import os

@tool
def search_tool(query: str) -> str:
    """Search the internet for up-to-date information using Tavily API."""
    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        result = tavily.search(query=query)
        return result['results'][0]['content']
    except Exception as e:
        return f"Search failed: {str(e)}"
