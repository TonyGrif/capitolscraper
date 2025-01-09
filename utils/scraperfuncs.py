"""This module contains utility functions for the scraper module"""

import httpx
from bs4 import BeautifulSoup

from .dataclasses import PageData, TradesStats


def make_request(page: str) -> httpx.Response:
    """Make a request on capitoltrades

    Args:
        page: The page to make a request on, valid options are: \"trades\"

    Raises:
        HTTPStatusError on unsuccessful status code
    """
    res = httpx.get(f"https://www.capitoltrades.com/{page}")
    res.raise_for_status()
    return res


def parse_page_data(text: str) -> PageData:
    """Parse the page for page specific data"""
    soup = BeautifulSoup(text, "html.parser")

    elem = soup.find(
        "p",
        {"class": "hidden leading-7 sm:block"},
    )

    nums = elem.find_all("b")  # type: ignore

    data = [int(num.text) for num in nums]
    return PageData(*data)


def parse_trade_stats(text: str) -> TradesStats:
    """Parse the page for trade stats"""
    soup = BeautifulSoup(text, "html.parser")

    elems = soup.find_all(
        "div",
        {"class": "text-size-5 font-medium leading-6 text-txt"},
    )

    data = [elem.text for elem in elems]
    return TradesStats(
        int(data[0].replace(",", "")),
        int(data[1].replace(",", "")),
        data[2],
        int(data[3].replace(",", "")),
        int(data[4].replace(",", "")),
    )
