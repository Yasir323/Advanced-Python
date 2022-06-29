"""
Barrier
A threading.Barrier can be used to keep a fixed number of 
threads in sync. When creating a Barrier, the caller must 
specify how many threads will be synchronizing on it. Each 
thread calls .wait() on the Barrier. They all will remain 
blocked until the specified number of threads are waiting, 
and then the are all released at the same time.

Remember that threads are scheduled by the operating system 
so, even though all of the threads are released simultaneously, 
they will be scheduled to run one at a time.

One use for a Barrier is to allow a pool of threads to 
initialize themselves. Having the threads wait on a Barrier 
after they are initialized will ensure that none of the 
threads start running before all of the threads are finished 
with their initialization.
"""
