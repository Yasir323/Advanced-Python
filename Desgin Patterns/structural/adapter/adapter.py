import math


# Say you have two classes with compatible interfaces:
# RoundHole and RoundPeg.
class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        # Return the radius of the peg.
        return self.radius


class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        # Return the radius of the hole.
        return self.radius

    def fits(self, peg: RoundPeg):
        return self.get_radius() >= peg.get_radius()


# But there's an incompatible class: SquarePeg.
class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        # Return the square peg width.
        return self.width


# An adapter class lets you fit square pegs into round holes.
# It extends the RoundPeg class to let the adapter objects act
# as round pegs.
class SquarePegAdapter(RoundPeg):
    """
    In reality, the adapter contains an instance of the SquarePeg class.
    """
    def __init__(self, peg: SquarePeg):
        self.__peg = peg
        super().__init__(self.__peg.get_width())

    def get_radius(self):
        """
        The adapter pretends that it's a round peg with a
        radius that could fit the square peg that the adapter
        actually wraps.
        """
        return self.__peg.get_width() * math.sqrt(2) / 2


# Somewhere in client code.
hole = RoundHole(5)
rpeg = RoundPeg(5)
print(hole.fits(rpeg))  # true

small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)
try:
    print(hole.fits(small_sqpeg))  # this won't compile (incompatible types)
except AttributeError:
    print("Incompatible interfaces!!!!")
small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
print(hole.fits(small_sqpeg_adapter))  # true
print(hole.fits(large_sqpeg_adapter))  # false
