import asyncio
import queue
import random

q = queue.Queue()
is_finished = False

def gen():
    for i in range(10):
        print(f"Yielding {i}")
        yield i

async def producer():
    for i in gen():
        print(f"Put {i}")
        q.put(i)
        await asyncio.sleep(1)
    global is_finished
    is_finished = True

async def consumer():
    print('Inside consumer')
    while not is_finished:
        if q.qsize() > 2:
            while not q.empty():
                i = q.get()
                print(f"Consumed {i}")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(producer(), consumer())

if __name__ == '__main__':
    asyncio.run(main())