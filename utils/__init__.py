"""This module contains utility functions for this project"""

from .scraperfuncs import make_request, parse_page_data, parse_trade_stats

__all__ = ["make_request", "parse_trade_stats", "parse_page_data"]
