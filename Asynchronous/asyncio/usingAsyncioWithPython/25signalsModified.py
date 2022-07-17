import asyncio
from signal import SIGINT, SIGTERM


async def main():
    try:
        while True:
            print('<Your app is running>')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        """
        This time, our main() coroutine is going to do some cleanup internally. When
        the cancellation signal is received (initiated by cancelling each of the tasks), there
        will be a period of 3 seconds where main() will continue running during the
        run_until_complete() phase of the shutdown process. It’ll print, "Your app is
        shutting down…".
        """
        for i in range(3):
            print('<Your app is shutting down...>')
            await asyncio.sleep(1)


def handler(sig):
    """
    This is a callback handler for when we receive a signal.
    """
    loop.stop()
    """
    The primary purpose of the handler is to stop the loop: this will unblock the
    loop.run_forever() call and allow pending task collection and cancellation, and
    the run_complete() for shutdown.
    """
    print(f'Got signal: {sig!s}, shutting down.')
    loop.remove_signal_handler(SIGTERM)
    """
    Since we are now in shutdown mode, we don’t want another SIGINT or SIGTERM
    to trigger this handler again: that would call loop.stop() during the
    run_until_complete() phase, which would interfere with our shutdown pro‐
    cess. Therefore, we remove the signal handler for SIGTERM from the loop.
    """
    loop.add_signal_handler(SIGINT, lambda: None)
    """
    This is a “gotcha”: we can’t simply remove the handler for SIGINT, because if we
    did that, KeyboardInterrupt would again become the handler for SIGINT, the
    same as it was before we added our own handlers. Instead, we set an empty
    lambda function as the handler. This means that KeyboardInterrupt stays away,
    and SIGINT (and Ctrl-C) has no effect.
    """


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for sig in (SIGTERM, SIGINT):
        loop.add_signal_handler(sig, handler, sig)
    loop.create_task(main())
    loop.run_forever()
    """
    Execution blocks on run_forever() until something stops the loop. In
    this case, the loop will be stopped inside handler() if either SIGINT or SIGTERM is
    sent to our process.
    """
    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()
