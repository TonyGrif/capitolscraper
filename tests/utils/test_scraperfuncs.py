import pytest
from pathlib import Path

from utils import make_request, parse_trade_stats


@pytest.fixture
def res():
    return make_request()


@pytest.fixture
def page():
    return Path("tests/resources/01-02-2025_tradepage.txt")


def test_make_request(res):
    assert res.status_code == 200
    assert res.text is not None


def test_parse_trade_stats(page):
    with open(page, "r") as f:
        data = parse_trade_stats(str(f.readlines()))
        assert len(data) == 5

        assert data[0] == "35,791"
        assert data[1] == "1,743"
        assert data[2] == "$2.161B"
        assert data[3] == "204"
        assert data[4] == "3,147"
