import asyncio
import socket
from keyword import kwlist
from typing import Tuple

MAX_KEYWORD_LEN = 4  # <1>


async def probe(domain: str) -> Tuple[str, bool]:  # <2>
    loop = asyncio.get_running_loop()  # <3>
    try:
        # The loop.getaddrinfo(…) coroutine-method returns a five-part
        # tuple of parameters to connect to the given address using a socket. In
        # this example, we don’t need the result. If we got it, the domain resolves;
        # otherwise, it doesn’t.
        await loop.getaddrinfo(domain, None)  # <4>
    except socket.gaierror:
        return domain, False
    return domain, True


async def main() -> None:  # <5>
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() for name in names)  # <7>
    # Build a list of coroutine objects by invoking the probe coroutine with
    # each domain argument.
    coros = [probe(domain) for domain in domains]  # <8>
    # asyncio.as_completed is a generator that yields the coroutines in
    # the order they are completed—not the order they were submitted.
    for coro in asyncio.as_completed(coros):  # <9>
        domain, found = await coro  # <10>
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())  # <11>
