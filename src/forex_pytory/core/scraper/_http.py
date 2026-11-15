import logging
from urllib.parse import urlparse
import cloudscraper

logger = logging.getLogger(__name__)


def get_page_html(url, timeout=10):
    """Fetch page HTML using cloudscraper and return the source text.

    Raises RuntimeError on network errors (keeps behaviour of previous scrapers).
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(
            f"Invalid URL scheme: {parsed.scheme!r}. Only HTTP and HTTPS are allowed."
        )

    scraper = cloudscraper.create_scraper()
    try:
        resp = scraper.get(url, timeout=timeout)
        resp.raise_for_status()
    except Exception as e:
        logger.exception("Failed to fetch page HTML")
        raise RuntimeError(f"Failed to get URL {url}: {e}")

    return resp.text
