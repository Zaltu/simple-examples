from threading import Thread
import asyncio




async def test(index, waittime):
    """
    Launch an asyncio subprocess.

    :param AigisPlugin plugin: the plugin
    """
    await asyncio.sleep(waittime)
    print("Hello World " + index)
    checkForLoop(index)

def checkForLoop(index):
    try:
        asyncio.get_running_loop()
        print("Running loop " + index)
    except RuntimeError:  # No running loop
        print("No running loop " + index)


# Setup the asyncio event loop for subprocess management
ALOOP = asyncio.new_event_loop()
ALOOP.run_until_complete(test('NA', 0))
ALOOP_FOREVER = Thread(target=ALOOP.run_forever)
ALOOP_FOREVER.start()

# Setup the asyncio event loop for subprocess management
BLOOP = asyncio.new_event_loop()
BLOOP_FOREVER = Thread(target=BLOOP.run_forever)
BLOOP_FOREVER.start()

asyncio.get_event_loop().run_until_complete(test('NB', 0))

checkForLoop("MAIN")

fut = asyncio.run_coroutine_threadsafe(test('A', 4), ALOOP)
fut.result()
asyncio.run_coroutine_threadsafe(test('B', 2), BLOOP)

print("Done")