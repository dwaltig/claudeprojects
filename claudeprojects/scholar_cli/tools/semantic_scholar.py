"""
Semantic Scholar API wrapper.
Provides access to academic paper search and citation graphs.
"""
import requests
import time
from typing import List, Optional
from ..config import SEMANTIC_SCHOLAR_API_KEY

BASE_URL = "https://api.semanticscholar.org/graph/v1"

def _get_headers():
    """Get headers with optional API key."""
    headers = {}
    if SEMANTIC_SCHOLAR_API_KEY:
        headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY
    return headers

def _rate_limit():
    """Simple rate limiting - 1 req/sec without key."""
    if not SEMANTIC_SCHOLAR_API_KEY:
        time.sleep(1.1)

def search_papers(
    query: str,
    limit: int = 10,
    fields: Optional[List[str]] = None
) -> List[dict]:
    """
    Search for papers by keyword.
    
    Args:
        query: Search query
        limit: Max results (default 10)
        fields: Fields to return (default: title, abstract, year, authors, citationCount, url)
    
    Returns:
        List of paper dicts
    """
    if fields is None:
        fields = ["title", "abstract", "year", "authors", "citationCount", "url", "externalIds"]
    
    _rate_limit()
    
    response = requests.get(
        f"{BASE_URL}/paper/search",
        headers=_get_headers(),
        params={
            "query": query,
            "limit": limit,
            "fields": ",".join(fields)
        }
    )
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])


def get_paper(paper_id: str, fields: Optional[List[str]] = None) -> dict:
    """
    Get detailed info about a specific paper.
    
    Args:
        paper_id: Semantic Scholar paper ID, DOI, or ArXiv ID
        fields: Fields to return
    
    Returns:
        Paper dict
    """
    if fields is None:
        fields = ["title", "abstract", "year", "authors", "citationCount", "referenceCount", "url", "externalIds"]
    
    _rate_limit()
    
    response = requests.get(
        f"{BASE_URL}/paper/{paper_id}",
        headers=_get_headers(),
        params={"fields": ",".join(fields)}
    )
    response.raise_for_status()
    return response.json()


def get_citations(
    paper_id: str,
    limit: int = 10,
    min_citations: int = 5
) -> List[dict]:
    """
    Get papers that cite the given paper.
    
    Args:
        paper_id: Semantic Scholar paper ID
        limit: Max results
        min_citations: Filter for high-impact citing papers
    
    Returns:
        List of citing paper dicts
    """
    _rate_limit()
    
    response = requests.get(
        f"{BASE_URL}/paper/{paper_id}/citations",
        headers=_get_headers(),
        params={
            "limit": limit * 2,  # Fetch extra to filter
            "fields": "title,abstract,year,authors,citationCount,url"
        }
    )
    response.raise_for_status()
    data = response.json()
    
    # Filter for high-impact papers
    citations = [
        c["citingPaper"] for c in data.get("data", [])
        if c["citingPaper"].get("citationCount", 0) >= min_citations
    ]
    return citations[:limit]


def get_references(paper_id: str, limit: int = 10) -> List[dict]:
    """
    Get papers that the given paper cites.
    """
    _rate_limit()
    
    response = requests.get(
        f"{BASE_URL}/paper/{paper_id}/references",
        headers=_get_headers(),
        params={
            "limit": limit,
            "fields": "title,abstract,year,authors,citationCount,url"
        }
    )
    response.raise_for_status()
    data = response.json()
    return [r["citedPaper"] for r in data.get("data", [])]
