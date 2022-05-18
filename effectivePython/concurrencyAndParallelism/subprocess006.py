import time
import subprocess

"""
If I’m worried about the child processes never finishing or somehow
blocking on input or output pipes, I can pass the timeout parameter
to the communicate method. This causes an exception to be raised if
the child process hasn’t finished within the time period, giving me a
chance to terminate the misbehaving subprocess:
"""
proc = subprocess.Popen(['timeout', '1'], shell=True)
try:
    proc.communicate(timeout=2)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

while proc.poll() is None:
    print('Working...')
    time.sleep(0.1)
print('Exit status', proc.poll())
