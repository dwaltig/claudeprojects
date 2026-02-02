"""
Scholar CLI - Academic Research from the Terminal
Usage: python -m scholar_cli "your research query"
"""
import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich import print as rprint

from .tools import exa_search, semantic_scholar, arxiv_search
from .config import check_keys

console = Console()

def format_authors(authors: list, max_display: int = 3) -> str:
    """Format author list, truncating if too long."""
    if not authors:
        return "Unknown"
    if isinstance(authors[0], dict):
        names = [a.get("name", "Unknown") for a in authors]
    else:
        names = authors
    
    if len(names) > max_display:
        return ", ".join(names[:max_display]) + f" (+{len(names) - max_display} more)"
    return ", ".join(names)


def display_results(results: list, source: str):
    """Display search results in a Rich table."""
    if not results:
        console.print(f"[yellow]No results found from {source}[/yellow]")
        return
    
    table = Table(title=f"📚 Results from {source}", show_lines=True)
    table.add_column("#", style="dim", width=3)
    table.add_column("Title", style="bold cyan", max_width=50)
    table.add_column("Authors", max_width=30)
    table.add_column("Year", justify="center", width=6)
    table.add_column("Citations", justify="right", width=8)
    
    for i, paper in enumerate(results, 1):
        # Handle different result formats
        title = paper.get("title", "Untitled")
        authors = format_authors(paper.get("authors", []))
        year = str(paper.get("year", paper.get("published", "N/A")))[:4]
        citations = paper.get("citationCount", "—")
        if citations != "—":
            citations = str(citations)
        
        table.add_row(str(i), title, authors, year, citations)
    
    console.print(table)
    
    # Print URLs for easy access
    console.print("\n[bold]URLs:[/bold]")
    for i, paper in enumerate(results, 1):
        url = paper.get("url", paper.get("pdf_url", "N/A"))
        console.print(f"  [{i}] {url}")


def search_all(query: str, limit: int = 5):
    """Search across all sources and display combined results."""
    console.print(Panel(f"[bold]Searching:[/bold] {query}", style="blue"))
    
    # Exa Neural Search (Web/Academic)
    console.print("\n[dim]Searching Exa (Neural Web Search)...[/dim]")
    try:
        exa_results = exa_search.search_academic(query, num_results=limit)
        formatted = [
            {"title": r.get("title"), "url": r.get("url"), "published": r.get("publishedDate", ""), "authors": []}
            for r in exa_results.get("results", [])
        ]
        display_results(formatted, "Exa Neural Search")
    except Exception as e:
        console.print(f"[red]Exa error: {e}[/red]")
    
    # Semantic Scholar
    console.print("\n[dim]Searching Semantic Scholar...[/dim]")
    try:
        ss_results = semantic_scholar.search_papers(query, limit=limit)
        display_results(ss_results, "Semantic Scholar")
    except Exception as e:
        console.print(f"[red]Semantic Scholar error: {e}[/red]")
    
    # ArXiv
    console.print("\n[dim]Searching ArXiv...[/dim]")
    try:
        arxiv_results = arxiv_search.search_papers(query, max_results=limit)
        display_results(arxiv_results, "ArXiv")
    except Exception as e:
        console.print(f"[red]ArXiv error: {e}[/red]")


def search_single_source(query: str, source: str, limit: int = 10):
    """Search a specific source."""
    console.print(Panel(f"[bold]Searching {source}:[/bold] {query}", style="blue"))
    
    if source == "exa":
        results = exa_search.search_academic(query, num_results=limit)
        formatted = [
            {"title": r.get("title"), "url": r.get("url"), "published": r.get("publishedDate", ""), "authors": []}
            for r in results.get("results", [])
        ]
        display_results(formatted, "Exa")
    elif source == "semantic":
        results = semantic_scholar.search_papers(query, limit=limit)
        display_results(results, "Semantic Scholar")
    elif source == "arxiv":
        results = arxiv_search.search_papers(query, max_results=limit)
        display_results(results, "ArXiv")
    else:
        console.print(f"[red]Unknown source: {source}. Use: exa, semantic, arxiv[/red]")


def cite_crawl(paper_id: str, limit: int = 10):
    """Crawl citations for a given paper."""
    console.print(Panel(f"[bold]Citation Crawl:[/bold] {paper_id}", style="green"))
    
    # Get the seed paper
    console.print("\n[dim]Fetching seed paper...[/dim]")
    try:
        seed = semantic_scholar.get_paper(paper_id)
        console.print(f"[bold cyan]{seed.get('title')}[/bold cyan]")
        console.print(f"Citations: {seed.get('citationCount', 'N/A')} | References: {seed.get('referenceCount', 'N/A')}")
    except Exception as e:
        console.print(f"[red]Error fetching paper: {e}[/red]")
        return
    
    # Get citing papers
    console.print("\n[dim]Fetching papers that cite this work...[/dim]")
    try:
        citations = semantic_scholar.get_citations(paper_id, limit=limit)
        display_results(citations, "Citing Papers")
    except Exception as e:
        console.print(f"[red]Error fetching citations: {e}[/red]")


def main():
    parser = argparse.ArgumentParser(
        description="Scholar CLI - Academic Research from the Terminal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m scholar_cli "Buddhist epistemology"
  python -m scholar_cli "Lotus Sutra translations" --source arxiv
  python -m scholar_cli --citations "DOI:10.1234/example"
  python -m scholar_cli --check-keys
        """
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--source", "-s", choices=["exa", "semantic", "arxiv"], 
                        help="Search specific source only")
    parser.add_argument("--limit", "-n", type=int, default=5, 
                        help="Number of results per source (default: 5)")
    parser.add_argument("--citations", "-c", metavar="PAPER_ID",
                        help="Crawl citations for a paper (use DOI or Semantic Scholar ID)")
    parser.add_argument("--check-keys", action="store_true",
                        help="Check API key configuration")
    
    args = parser.parse_args()
    
    if args.check_keys:
        check_keys()
        return
    
    if args.citations:
        cite_crawl(args.citations, args.limit)
        return
    
    if not args.query:
        parser.print_help()
        return
    
    if args.source:
        search_single_source(args.query, args.source, args.limit)
    else:
        search_all(args.query, args.limit)


if __name__ == "__main__":
    main()
