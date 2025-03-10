import time
from pathlib import Path
from typing import Callable, List

import httpx  # <1>

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
DEST_DIR = Path('downloaded')                         # <4>


def save_flag(img: bytes, filename: str) -> None:     # <5>
    (DEST_DIR / filename).write_bytes(img)


def get_flag(cc: str) -> bytes:  # <6>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1,       # <7>
                     allow_redirects=True)  # <8>
    resp.raise_for_status()  # <9>
    return resp.content


def download_many(cc_list: List[str]) -> int:  # <10>
    for cc in sorted(cc_list):                 # <11>
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ', flush=True)         # <12>
    return len(cc_list)


def main(downloader: Callable[[List[str]], int]) -> None:  # <13>
    DEST_DIR.mkdir(exist_ok=True)                          # <14>
    t0 = time.perf_counter()                               # <15>
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')


if __name__ == '__main__':
    main(download_many)     # <16>
