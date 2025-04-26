import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def research(query: str) -> str:
    """
    Uses Tavily API to search for information online and return summarized content.
    """
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results = client.search(query=query, search_depth="advanced", max_results=5)
    return "\n\n".join([r['content'] for r in results['results']])