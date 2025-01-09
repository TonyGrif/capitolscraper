"""This module contains utility functions for the scraper module"""

from typing import List

import httpx
from bs4 import BeautifulSoup

from .dataclasses import PageData, Politician, Trade, TradesStats


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


def parse_trade_page(text: str) -> List[Trade]:
    """Parse the trades found within a page"""
    soup = BeautifulSoup(text, "html.parser")
    trades = soup.find_all(
        "tr",
        {
            "class": "border-b transition-colors hover:bg-neutral-100/50 data-[state=selected]:bg-neutral-100 dark:hover:bg-neutral-800/50 dark:data-[state=selected]:bg-neutral-800 h-14 border-primary-15"
        },
    )

    return [_parse_trade(trade) for trade in trades]


def _parse_trade(trade) -> Trade:
    pol_block = trade.find(
        "div",
        {"class": "q-cell cell--politician has-avatar"},
    )

    return Trade(_parse_politician(pol_block.text))


def _parse_politician(text: str) -> Politician:
    if "Democrat" in text:
        party = "Democrat"
        text = text.replace("Democrat", " ")
    elif "Republican" in text:
        party = "Republican"
        text = text.replace("Republican", " ")
    else:
        party = "Independent"
        text = text.replace("Other", " ")

    if "House" in text:
        chamber = "House"
        text = text.replace("House", "")
    else:
        chamber = "Senate"
        text = text.replace("Senate", "")

    return Politician(text[0:-2].strip(), party, chamber, text[-2:])


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
