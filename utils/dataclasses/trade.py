"""This module contains a Trade dataclass"""

from dataclasses import dataclass

from .traded_issuer import IssuedTrader


@dataclass
class Politician:
    """Contains data pertaining to a politician

    Args:
        name: The politician's name
        party: The politician's party affiliation
        chamber: The chamber of this politician
        state: The state of this politician
    """

    name: str
    party: str
    chamber: str
    state: str


@dataclass
class Dates:
    """Contains data pertaining to a trade's dates

    Args:
        published: When the trade was published
        traded: The data this trade was executed
        filed_after: How long this trade was published from when it was executed
    """

    published: str
    traded: str
    filed_after: int


@dataclass
class Trade:
    """Contains data pertaining to a single trade

    Args:
        politician: A dataclass of politician data
        issuer: The issuer of this trade
        dates: Dates associated with this trade
        owner: The owner of this trade move
    """

    politician: Politician
    issuer: IssuedTrader
    dates: Dates
    owner: str
