"""
Launch a subprocess to log a value to a file, and then wait for that subprocess to complete asynchroneously.
"""
import asyncio

async def asyncwait(aproc, filehandler):
    """
    Use the asyncio module's wait for long-running processes to complete.
    """
    print("starting async wait")
    await aproc.wait()
    print("process complete, closing file handle")
    filehandler.close()
    print("finished")

async def asyncpopen():
    """
    Use the async popen function since we need an async module process object to run the async wait.
    """
    filehandler = open("test.log", 'a+')
    aproc = await asyncio.create_subprocess_exec("python", "torun.py", stdout=filehandler)
    asyncio.ensure_future(asyncwait(aproc, filehandler))

# Run the function to launch the subprocess
ALOOP = asyncio.get_event_loop()
ALOOP.run_until_complete(asyncpopen())
print("ran")

print("main thread complete")
