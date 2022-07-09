# Typical usage

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    ...
    # Do work in parallel
    ...
    pass

"""
Under the covers, a ProcessPoolExecutor creates N independent running Python interpreters
where N is the number of available CPUs detected on the system. You can change the
number of processes created by supplying an optional argument to ProcessPoolExecutor(N).
The pool runs until the last statement in the with block is executed, at which point
the process pool is shut down. However, the program will wait until all submitted work has been processed.

Work to be submitted to a pool must be defined in a function. There are two methods
for submission. If you are trying to parallelize a list comprehension or a map()
operation, you use pool.map():
"""


# A function that performs a lot of work
def work(x):
    result_ = x * 2
    ...
    return result_


data = []
# Non-parallel code
results = map(work, data)

# Parallel implementation
with ProcessPoolExecutor() as executor:
    result = executor.map(work, data)


# Alternatively, you can manually submit single tasks using the pool.submit() method:

with ProcessPoolExecutor() as executor:
    future = executor.submit(work, data)
    # Obtain the result
    res = future.result()  # Blocking

"""
If you manually submit a job, the result is an instance of Future. To obtain the actual
result, you call its result() method. This blocks until the result is computed and returned by the pool.

Instead of blocking, you can also arrange to have a callback function triggered upon
completion instead. For example:
"""


def when_done(future_):
    print(f"Got: {future_.result()}")


with ProcessPoolExecutor() as executor:
    future_result = executor.submit(work, data)
    future_result.add_done_callback(when_done)

"""
The user-supplied callback function receives an instance of Future that must be used
to obtain the actual result (i.e., by calling its result() method).
"""