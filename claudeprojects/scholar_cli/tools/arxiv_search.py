"""
ArXiv API wrapper.
Provides access to preprints in physics, math, CS, and related fields.
"""
import arxiv
from typing import List, Optional

def search_papers(
    query: str,
    max_results: int = 10,
    sort_by: str = "relevance"
) -> List[dict]:
    """
    Search ArXiv for papers.
    
    Args:
        query: Search query (supports ArXiv search syntax)
        max_results: Maximum number of results
        sort_by: "relevance", "submitted", or "updated"
    
    Returns:
        List of paper dicts with title, abstract, authors, url, published
    """
    sort_criterion = {
        "relevance": arxiv.SortCriterion.Relevance,
        "submitted": arxiv.SortCriterion.SubmittedDate,
        "updated": arxiv.SortCriterion.LastUpdatedDate
    }.get(sort_by, arxiv.SortCriterion.Relevance)
    
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sort_criterion
    )
    
    results = []
    for paper in client.results(search):
        results.append({
            "title": paper.title,
            "abstract": paper.summary,
            "authors": [a.name for a in paper.authors],
            "url": paper.entry_id,
            "pdf_url": paper.pdf_url,
            "published": paper.published.strftime("%Y-%m-%d"),
            "categories": paper.categories,
            "arxiv_id": paper.entry_id.split("/")[-1]
        })
    
    return results


def get_paper_by_id(arxiv_id: str) -> Optional[dict]:
    """
    Get a specific paper by ArXiv ID.
    
    Args:
        arxiv_id: ArXiv ID (e.g., "2301.00001" or "cs.AI/0001001")
    
    Returns:
        Paper dict or None if not found
    """
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    
    try:
        paper = next(client.results(search))
        return {
            "title": paper.title,
            "abstract": paper.summary,
            "authors": [a.name for a in paper.authors],
            "url": paper.entry_id,
            "pdf_url": paper.pdf_url,
            "published": paper.published.strftime("%Y-%m-%d"),
            "categories": paper.categories
        }
    except StopIteration:
        return None
