from functools import partialmethod


class Live:

    def __init__(self):
        self._live = False

    def set_live(self,state:'bool'):
        self._live = state

    def __get_live(self):
        return self._live

    def __call__(self):
        # enable this to be called when the object is made callable.
        return self.__get_live()

    # partial methods. Freezes the method `set_live` and `set_dead`
    # with the specific arguments
    set_alive = partialmethod(set_live, True)
    set_dead = partialmethod(set_live, False)


live = Live() # create object
print(live()) # make the object callable. It calls `__call__` under the hood
live.set_alive() # Call the partial method
print(live())
