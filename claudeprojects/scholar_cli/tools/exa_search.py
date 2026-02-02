"""
Exa.ai Neural Search wrapper.
Provides semantic search across the web with domain filtering.
"""
import requests
from typing import List, Optional
from ..config import EXA_API_KEY

EXA_BASE_URL = "https://api.exa.ai"

def search(
    query: str,
    num_results: int = 10,
    include_domains: Optional[List[str]] = None,
    exclude_domains: Optional[List[str]] = None,
    start_published_date: Optional[str] = None,
) -> dict:
    """
    Search using Exa's neural search.
    
    Args:
        query: Natural language search query
        num_results: Number of results to return
        include_domains: List of domains to include (e.g., ["arxiv.org", "nih.gov"])
        exclude_domains: List of domains to exclude
        start_published_date: Filter for recent content (e.g., "2024-01-01")
    
    Returns:
        Dict with 'results' list containing title, url, published_date, text
    """
    if not EXA_API_KEY:
        raise ValueError("EXA_API_KEY not set. Add it to scholar_cli/.env")
    
    headers = {
        "x-api-key": EXA_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": query,
        "numResults": num_results,
        "type": "neural",  # Use semantic search
        "contents": {
            "text": {"maxCharacters": 2000}  # Get text snippets
        }
    }
    
    if include_domains:
        payload["includeDomains"] = include_domains
    if exclude_domains:
        payload["excludeDomains"] = exclude_domains
    if start_published_date:
        payload["startPublishedDate"] = start_published_date
    
    response = requests.post(
        f"{EXA_BASE_URL}/search",
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json()


def search_academic(query: str, num_results: int = 10) -> dict:
    """
    Search specifically in academic domains.
    """
    academic_domains = [
        "arxiv.org",
        "semanticscholar.org", 
        "ncbi.nlm.nih.gov",
        "jstor.org",
        "springer.com",
        "wiley.com",
        "tandfonline.com",
        "cambridge.org",
        "oxford.com"
    ]
    return search(query, num_results, include_domains=academic_domains)
