"""Fetch and clean visible text from web pages (and PDFs) for the college FAQ chatbot."""

import io

import pdfplumber
import requests
from bs4 import BeautifulSoup

# Custom User-Agent so the request looks like a real browser rather than a bot
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

# Tags that hold no useful FAQ content — stripped before extracting text
TAGS_TO_REMOVE = ["script", "style", "nav", "footer", "header", "noscript"]


def _normalize(text: str) -> str:
    """Collapse runs of spaces/newlines into clean single-spaced text."""
    return " ".join(text.split())


def _extract_pdf_text(content: bytes) -> str:
    """Extract text from raw PDF bytes using pdfplumber."""
    # Wrap the bytes in a file-like object so pdfplumber can open it
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        # Pull text from every page, skipping pages that yield nothing
        pages = [page.extract_text() or "" for page in pdf.pages]
    return "\n".join(pages)


def _extract_html_text(html: str) -> str:
    """Extract visible text from HTML using BeautifulSoup."""
    # Parse the HTML using Python's built-in parser
    soup = BeautifulSoup(html, "html.parser")

    # Drop tags that contain scripts, styling, or page chrome (nav/header/footer)
    for tag in soup(TAGS_TO_REMOVE):
        tag.decompose()

    # Extract all remaining visible text, using spaces to join separate elements
    return soup.get_text(separator=" ")


def get_page_text(url: str) -> str | None:
    """Fetch a URL and return its cleaned visible text, or None on any failure.

    Handles both HTML pages and PDF documents — PDFs are detected via the
    Content-Type header (with a magic-bytes fallback) and parsed with pdfplumber.
    """
    try:
        # Fetch the page with a custom header and a 10-second timeout
        response = requests.get(url, headers=HEADERS, timeout=10)
    except requests.RequestException:
        # Covers timeouts, connection errors, and any other request failure
        return None

    # Treat anything other than HTTP 200 as a failure
    if response.status_code != 200:
        return None

    # Decide whether this is a PDF: trust the Content-Type, fall back to the
    # %PDF magic bytes in case the server reports a generic/incorrect type
    content_type = response.headers.get("Content-Type", "").lower()
    is_pdf = "application/pdf" in content_type or response.content[:5] == b"%PDF-"

    try:
        # Route to the right extractor based on the content type
        if is_pdf:
            raw_text = _extract_pdf_text(response.content)
        else:
            raw_text = _extract_html_text(response.text)
    except Exception:
        # Never crash on a malformed page or unreadable PDF
        return None

    # Normalize whitespace, then return None if nothing meaningful is left
    text = _normalize(raw_text)
    return text if text else None


if __name__ == "__main__":
    # Fetch and print the placements page text (this URL serves a PDF)
    placement_text = get_page_text("https://pragati.ac.in/placements")
    print(placement_text)
