from pathlib import Path

import httpx
import pytest

from utils import make_request, parse_trade_stats


@pytest.fixture
def tradepage():
    return Path("tests/resources/01-02-2025_tradepage.txt")


def test_make_request():
    res = make_request("trades")
    assert res.status_code == 200
    assert res.text is not None

    with pytest.raises(httpx.HTTPStatusError):
        res = make_request("notreal")


def test_parse_trade_stats(tradepage):
    with open(tradepage, "r") as f:
        data = parse_trade_stats(str(f.readlines()))
        assert len(data) == 5

        assert data[0] == "35,791"
        assert data[1] == "1,743"
        assert data[2] == "$2.161B"
        assert data[3] == "204"
        assert data[4] == "3,147"
