import asyncio
from threading import Thread

import nest_asyncio

nest_asyncio.apply()

# Setup the asyncio event loop for subprocess management
ALOOP = asyncio.new_event_loop()
ALOOP_FOREVER = Thread(target=ALOOP.run_forever)
ALOOP_FOREVER.start()

async def a():
    print('A')


async def b(fut):
    print("Awating A")
    await fut
    print('B')
    asyncio.create_task(c())

async def c():
    print('C')

async def globa():
    fut = asyncio.create_task(a())
    asyncio.create_task(b(fut))

asyncio.run_coroutine_threadsafe(globa(), ALOOP)
print("Done main")
