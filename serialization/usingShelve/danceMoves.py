class Move:

    def __init__(self, time, limb, what):
        self.time = time
        self.limb = limb
        self.what = what

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.time!r}, {self.limb!r}, {self.what!r})"
