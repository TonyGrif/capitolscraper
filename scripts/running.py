"""Running test for this project"""

import asyncio

from scraper import Trades

trades = Trades()


async def main():
    """Main driver"""
    _ = await trades.trades


asyncio.run(main())
