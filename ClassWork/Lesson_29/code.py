import asyncio
import aiohttp
import time
import random


URL = 'https://api.github.com/events'
MAX_CLIENTS = 3

async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print(f'Fetch process {pid}, asleep for {sleepy_time}')
    await asyncio.sleep(sleepy_time)

    async with aiohttp.request('GET', URL) as response:
        datetime = response.headers.get('Date')
    return f'Process {pid}:{datetime}, took: {time.time() - start} seconds'

async def asynchronus():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print(f'>>*{i + 1} {result}')
    print(f'Process took: {time.time() - start} seconds')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asynchronus())
    loop.close()