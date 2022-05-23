"""
You can also pipe data from a Python program into a subprocess and
retrieve its output. This allows you to utilize many other programs to
do work in parallel. For example, say that I want to use the openssl
command-line tool to encrypt some data. Starting the child process
with command-line arguments and I/O pipes is easy:
"""

import os
import subprocess


def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    process = subprocess.Popen(
        ['openssl', 'enc', '-pbkdf2', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    process.stdin.write(data)
    process.stdin.flush()  # Ensure that the child gets input
    return process

"""
Here, I pipe random bytes into the encryption function, but in practice
this input pipe would be fed data from user input, a file handle, a
network socket, and so on:
"""
processes = []
for _ in range(3):
    data = os.urandom(10)
    process = run_encrypt(data)
    processes.append(process)


"""
The child processes run in parallel and consume their input. Here,
I wait for them to finish and then retrieve their final output. The
output is random encrypted bytes as expected:
"""
for process in processes:
    out, _ = process.communicate()
    print(out[-10:])
