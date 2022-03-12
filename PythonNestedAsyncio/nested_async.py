"""
Example running an event loop within an event loop using nested asyncio.
"""
import asyncio

import nest_asyncio


async def wait_one():
    """First dummy wait function"""
    print("Starting One")
    await asyncio.sleep(1)
    asyncio.new_event_loop().run_until_complete(wait_two())
    print("One done!")


async def wait_two():
    """Second dummy wait function"""
    print("Starting Two")
    await asyncio.sleep(3)
    print("Two done!")


if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(wait_one())
