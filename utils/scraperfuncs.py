"""This module contains utility functions for the scraper module"""

from typing import Tuple

import httpx
from bs4 import BeautifulSoup


def make_request(page: str) -> httpx.Response:
    """Make a request on capitoltrades

    Args:
        page: The page to make a request on, valid options are: \"trades\"
    """
    return httpx.get(f"https://www.capitoltrades.com/{page}")


def parse_trade_stats(text: str) -> Tuple[str, str, str, str, str]:
    """Parse the page for trade stats"""
    soup = BeautifulSoup(text, "html.parser")

    elems = soup.find_all(
        "div",
        {"class": "text-size-5 font-medium leading-6 text-txt"},
    )

    vals = []
    for elem in elems:
        vals.append(elem.text)

    return tuple(vals)
