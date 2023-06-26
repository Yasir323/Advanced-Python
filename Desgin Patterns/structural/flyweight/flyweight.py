# The flyweight class contains a portion of the state of a
# tree. These fields store values that are unique for each
# particular tree. For instance, you won't find here the tree
# coordinates. But the texture and colors shared between many
# trees are here. Since this data is usually BIG, you'd waste a
# lot of memory by keeping it in each tree object. Instead, we
# can extract texture, color and other repeating data into a
# separate object which lots of individual tree objects can
# reference.
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        # 1. Create a bitmap of a given type, color & texture.
        # 2. Draw the bitmap on the canvas at X and Y coords.
        pass


# Flyweight factory decides whether to re-use existing
# flyweight or to create a new object.
class TreeFactory:
    treeTypes = {}  # Collection of tree types

    @staticmethod
    def getTreeType(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory.treeTypes:
            TreeFactory.treeTypes[key] = TreeType(name, color, texture)
        return TreeFactory.treeTypes[key]


# The contextual object contains the extrinsic part of the tree
# state. An application can create billions of these since they
# are pretty small: just two integer coordinates and one
# reference field.
class Tree:
    def __init__(self, x, y, treeType):
        self.x = x
        self.y = y
        self.type = treeType

    def draw(self, canvas):
        self.type.draw(canvas, self.x, self.y)


# The Tree and the Forest classes are the flyweight's clients.
# You can merge them if you don't plan to develop the Tree
# class any further.
class Forest:
    def __init__(self):
        self.trees = []  # Collection of Trees

    def plantTree(self, x, y, name, color, texture):
        treeType = TreeFactory.getTreeType(name, color, texture)
        tree = Tree(x, y, treeType)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)
