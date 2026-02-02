"""
Configuration loader for Scholar CLI.
Loads API keys from environment variables or .env file.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the scholar_cli directory
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

# API Keys
EXA_API_KEY = os.getenv("EXA_API_KEY")
SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

def check_keys():
    """Print status of API keys."""
    print(f"Exa API Key: {'✓ Set' if EXA_API_KEY else '✗ Missing'}")
    print(f"Semantic Scholar Key: {'✓ Set' if SEMANTIC_SCHOLAR_API_KEY else '○ Optional (using free tier)'}")
