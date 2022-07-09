"""
Program to read logs from a web server and find the IPs that accessed robot.txt
"""

import io
import glob
import gzip
import time
from concurrent.futures import ProcessPoolExecutor


def find_robots(filename):
    """
    Find all the hosts that access robots.txt in a single log file.
    """
    robots = set()
    with gzip.open(filename) as fp:
        for line in io.TextIOWrapper(fp, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots_proc(log_dir):
    """
    Find all hosts across and entire sequence of files
    """
    files = glob.glob(log_dir + '/*.log.gz')
    all_robots = set()
    with ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


def find_all_robots_sequential(log_dir):
    """
    Find all hosts across and entire sequence of files
    """
    files = glob.glob(log_dir + '/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    t1 = time.perf_counter()
    robots = find_all_robots_proc('logs')
    print(f"Time taken by threaded version: {time.perf_counter() - t1}")

    t2 = time.perf_counter()
    robots2 = find_all_robots_sequential('logs')
    print(f"Time taken by sequential version: {time.perf_counter() - t1}")
    for ipaddr in robots:
        print(ipaddr)
