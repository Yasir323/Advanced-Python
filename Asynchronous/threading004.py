import threading
import time


def thread_function(name):
    print(f"Thread {name} starting...")
    time.sleep(2)
    print(f"Thread {name} finishing...")


if __name__ == '__main__':
    print(f"Main\t: Before creating thread.")
    # A daemon thread will shut down immediately when the program exits.
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    print("Main\t: Before running thread.")
    x.start()
    print("Main\t: Waiting for thread to finish.")
    # x.join()
    print("Main\t: All done.")
