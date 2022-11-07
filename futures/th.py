from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import _thread


def temp(i):
    print('Going to Sleep ', i)
    if i == 9:
        # os._exit(1)
        _thread.interrupt_main()
    time.sleep(5)
    print(f'slept {i}')


threads = []
with ThreadPoolExecutor(max_workers=20) as executor:
    for i in range(20):
        threads.append(executor.submit(temp, i))
        print('Hello ', i)
    thread_count = 0
    for task in as_completed(threads):
        thread_count += 1
        print(f'Batch {thread_count}: Done')
