"""
It’s also possible to create chains of parallel processes, just like
UNIX pipelines, connecting the output of one child process to the
input of another, and so on. Here’s a function that starts the openssl
command-line tool as a subprocess to generate a Whirlpool hash of
the input stream:
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


def run_hash(input_stdin):
    return subprocess.Popen(
        ['openssl', 'dgst', '-whirlpool', '-binary'],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )
"""
Now, I can kick off one set of processes to encrypt some data and
another set of processes to subsequently hash their encrypted output.
Note that I have to be careful with how the stdout instance of the
upstream process is retained by the Python interpreter process that’s
starting this pipeline of child processes:
"""
encrypt_processes = []
hash_processes = []
for _ in range(3):
    data = os.urandom(100)
    encrypt_process = run_encrypt(data)
    encrypt_processes.append(encrypt_process)

    hash_process = run_hash(encrypt_process.stdout)
    hash_processes.append(hash_process)

    # Ensure that the child consumes the input stream and
    # the communicate() method doesn't inadvertently steal
    # input from the child. Also lets SIGPIPE propagate to
    # the upstream process if the downstream process dies.

    encrypt_process.stdout.close()
    encrypt_process.stdout = None


"""
The I/O between the child processes happens automatically once they
are started. All I need to do is wait for them to finish and print the
final output:
"""
for process in encrypt_processes:
    process.communicate()
    assert process.returncode == 0

for process in hash_processes:
    out, _ = process.communicate()
    print(out[-10:])
    assert process.returncode == 0
