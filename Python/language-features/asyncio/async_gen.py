import asyncio

q = queue.Queue()

async def async_gen():
    for i in range(5):
        print(f"Yielding {i}")
        yield i

async def async_emissary():
    async for i in async_gen():
        print(f"Writing {i}")
        q.put(i)

async def async_consumer(i):
    size = q.qsize()

    if size > 2:
        while q.empty():
            print(f"Consuming {q.get()}")

asyncio.run(async_emissary())
