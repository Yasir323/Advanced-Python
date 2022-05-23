"""
itertools.tee(iterable, n=2)

Return n independent iterators from a single iterable.
The following Python code helps explain what tee does (although 
the actual implementation is more complex and uses only a single 
underlying FIFO queue).

Roughly equivalent to:

def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    return
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)

Once tee() has made a split, the original iterable should not 
be used anywhere else; otherwise, the iterable could get advanced 
without the tee objects being informed.

tee iterators are not threadsafe. A RuntimeError may be raised 
when using simultaneously iterators returned by the same tee() 
call, even if the original iterable is threadsafe.
"""

import itertools as it

print(list(map(list, it.tee([1, 2, 34, 4, 5, 5, 4], 5))))
