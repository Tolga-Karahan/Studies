import asyncio
import random


async def waited(w_id):
    print(f"Waited {w_id}")
    print("Start sleeping")
    await asyncio.sleep(5)
    return f"Woke up {w_id}"


async def waiter(w_id):
    print(f"Waiter {w_id}")
    result = await waited(w_id)
    print(result)


async def main():
    await asyncio.gather(
        waiter(w_id=random.randint(0, 100)), waiter(w_id=random.randint(0, 100))
    )


if __name__ == "__main__":
    asyncio.run(main())
