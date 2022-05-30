"""
Under the covers, a ProcessPoolExecutor creates N independent running Python interpreters
where N is the number of available CPUs detected on the system. You can
change the number of processes created by supplying an optional argument to Proces
sPoolExecutor(N). The pool runs until the last statement in the with block is executed,
at which point the process pool is shut down. However, the program will wait until all
submitted work has been processed.

Work to be submitted to a pool must be defined in a function. There are two methods
for submission. If you are are trying to parallelize a list comprehension or a map()
operation, you use pool.map():

# A function that performs a lot of work
def work(x):
    ...
    return result

# Nonparallel code
results = map(work, data)

# Parallel implementation
with ProcessPoolExecutor() as pool:
    results = pool.map(work, data)

Alternatively, you can manually submit single tasks using the pool.submit() method:
# Some function
def work(x):
    ...
    return result

with ProcessPoolExecutor() as pool:
    ...
    # Example of submitting work to the pool
    future_result = pool.submit(work, arg)
    # Obtaining the result (blocks until done)
    r = future_result.result()

If you manually submit a job, the result is an instance of Future. To obtain the actual
result, you call its result() method. This blocks until the result is computed and returned
by the pool.
Instead of blocking, you can also arrange to have a callback function triggered upon
completion instead

"""

from concurrent.futures import ProcessPoolExecutor


def when_done(r):
    print('Got:', r.result())


def work(x):
    pass


with ProcessPoolExecutor() as pool:
    arg = 2
    future_result = pool.submit(work, arg)
    future_result.add_done_callback(when_done)

"""
Although process pools can be easy to use, there are a number of important considerations
to be made in designing larger programs. In no particular order:

• This technique for parallelization only works well for problems that can be trivially
decomposed into independent parts.
• Work must be submitted in the form of simple functions. Parallel execution of
instance methods, closures, or other kinds of constructs are not supported.
• Function arguments and return values must be compatible with pickle. Work is
carried out in a separate interpreter using interprocess communication. Thus, data
exchanged between interpreters has to be serialized.
Process pools are created by calling the fork() system call on Unix. This makes a
clone of the Python interpreter, including all of the program state at the time of the
fork. On Windows, an independent copy of the interpreter that does not clone state
is launched. The actual forking process does not occur until the first pool.map()
or pool.submit() method is called.

"""