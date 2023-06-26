from abc import ABC, abstractmethod


# The element interface declares an `accept` method that takes
# the base visitor interface as an argument.
class Shape(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def accept(self, v):
        pass


# Each concrete element class must implement the `accept`
# method in such a way that it calls the visitor's method that
# corresponds to the element's class.
class Dot(Shape):
    def accept(self, v):
        v.visitDot(self)


class Circle(Shape):
    def accept(self, v):
        v.visitCircle(self)


class Rectangle(Shape):
    def accept(self, v):
        v.visitRectangle(self)


class CompoundShape(Shape):
    def accept(self, v):
        v.visitCompoundShape(self)


# The Visitor interface declares a set of visiting methods that
# correspond to element classes. The signature of a visiting
# method lets the visitor identify the exact class of the
# element that it's dealing with.
class Visitor(ABC):
    @abstractmethod
    def visitDot(self, d):
        pass

    @abstractmethod
    def visitCircle(self, c):
        pass

    @abstractmethod
    def visitRectangle(self, r):
        pass

    @abstractmethod
    def visitCompoundShape(self, cs):
        pass


# Concrete visitors implement several versions of the same
# algorithm, which can work with all concrete element classes.
class XMLExportVisitor(Visitor):
    def visitDot(self, d):
        # Export the dot's ID and center coordinates.
        pass

    def visitCircle(self, c):
        # Export the circle's ID, center coordinates and radius.
        pass

    def visitRectangle(self, r):
        # Export the rectangle's ID, left-top coordinates, width, and height.
        pass

    def visitCompoundShape(self, cs):
        # Export the shape's ID as well as the list of its children's IDs.
        pass


# The client code can run visitor operations over any set of
# elements without figuring out their concrete classes. The
# accept operation directs a call to the appropriate operation
# in the visitor object.
class Application:
    def __init__(self):
        self.allShapes = []

    def export(self):
        exportVisitor = XMLExportVisitor()

        for shape in self.allShapes:
            shape.accept(exportVisitor)
