from threading import Thread
import asyncio
import sys
import nest_asyncio
import time

nest_asyncio.apply()


# Setup the asyncio event loop for subprocess management
ALOOP = asyncio.new_event_loop()
ALOOP_FOREVER = Thread(target=ALOOP.run_forever)
ALOOP_FOREVER.start()


async def test(index):
    """
    Launch an asyncio subprocess.

    :param AigisPlugin plugin: the plugin
    """
    print("Hello World " + index)
    _ext_proc = await asyncio.create_subprocess_exec(
        *[
            sys.executable,
            "-c", "import time;time.sleep(2);print('Sub done')"
        ]
    )
    await waitforsub(_ext_proc)
    print("Checkem")

async def waitforsub(index):
    print("Waiting for sub")
    await index.wait()
    print("Done waiting for sub")


async def normalwait():
    print("Sleeping...")
    time.sleep(2)
    print("Woke")

asyncio.run_coroutine_threadsafe(normalwait(), ALOOP)

asyncio.run_coroutine_threadsafe(test('A'), ALOOP)


print("Done")