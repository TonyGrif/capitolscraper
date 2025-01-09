"""This module contains a Trade dataclass"""

from dataclasses import dataclass


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
class Trade:
    """Contains data pertaining to a single trade

    Args:
        politician: A dataclass of politician data
    """

    politician: Politician
