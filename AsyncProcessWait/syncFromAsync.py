import asyncio
import time

async def notbackground():
    await asyncio.sleep(2)
    print("cool")

def issync():
    time.sleep(2)
    print("Hello World")


async def isasync():
    t = asyncio.ensure_future(notbackground())
    issync()
    await t


asyncio.get_event_loop().run_until_complete(isasync())
