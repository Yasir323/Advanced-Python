import time
import subprocess

proc = subprocess.Popen(['timeout', '1'], shell=True)

while proc.poll() is None:
    print('Working...')
    time.sleep(0.1)
print('Exit status', proc.poll())
