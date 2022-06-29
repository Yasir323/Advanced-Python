import asyncio


async def first_func():
    print('Inside 1st function.')
    print('One')
    await asyncio.sleep(1)
    print('Back inside 1st function.')
    print('Two')


async def second_func():
    print('Inside 2nd function.')
    print('One')
    print('Two')
    await asyncio.sleep(1)
    print('Back inside 2nd function.')
    print('Three')


async def third_func():
    print('Inside 3rd function.')
    print('One')
    print('Two')
    print('Three')
    await asyncio.sleep(1)
    print('Back inside 3rd function.')
    print('Four')


async def main():
    await asyncio.gather(first_func(), second_func(), third_func())


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
