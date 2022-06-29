import time
import threading


def thread_func(name):
    print(f"Thread {name} starting.")
    time.sleep(2)
    print(f"Thread {name} finishing.")


if __name__ == '__main__':
    threads = []
    for index in range(3):
        print(f"Main    : create and start thread {index}.")
        x = threading.Thread(target=thread_func, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print(f"Main    : before joining thread {index}")
        thread.join()
        print(f"Main    : thread {index} done.")
