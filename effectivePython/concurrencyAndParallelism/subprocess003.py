import time
import subprocess

start = time.perf_counter()
sleep_processes = []

for _ in range(10):
    process = subprocess.Popen(['timeout', '1'], shell=True)
    sleep_processes.append(process)
# Later, I wait for them to finish their I/O and terminate with the
# communicate method:
for process in sleep_processes:
    process.communicate()
end = time.perf_counter()
delta = end - start
print(f'Finished in {delta:.3} seconds')
