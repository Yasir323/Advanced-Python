import asyncio


async def f():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def g():
    print("A")
    # await asyncio.sleep(1)
    # for i in range(100_000_000):
    #     pass
    print("B")


async def h():
    print("a")
    await asyncio.sleep(0.1)
    print("b")


async def main():
    await asyncio.gather(f(), g(), h())


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
