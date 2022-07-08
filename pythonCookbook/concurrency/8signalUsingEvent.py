import time
from threading import Thread, Event


def countdown(n: int, start_evnt: Event) -> None:
    print('Starting countdown...')
    start_evnt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(0.1)


# Create the event object that will be used to signal startup of the thread.
start_event = Event()

# Launch the thread
print('Launching countdown...')
thread = Thread(target=countdown, args=(10, start_event))
thread.start()

# Wait for the thread to start (or event to trigger)
start_event.wait()
print('Countdown is running...')
