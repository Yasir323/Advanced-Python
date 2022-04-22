from functools import partial
from typing import Any


class NodeElement:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.count = 1  # For duplicate values


class BST:

    def __init__(self, value):
        self._root = NodeElement(value)
        self.insert = partial(self.insert, root=self._root)
        self.print_inorder = partial(self.print_inorder, node=self._root)

    def is_empty(self):
        if self._root is None:
            return True
        else:
            return False

    def insert(self, new_data: Any, root: NodeElement):
        if self._root is None:
            self._root = NodeElement(new_data)
        else:
            curr = root
            if new_data < curr.data:
                if curr.left:
                    curr = curr.left
                    self.insert(new_data, root=curr)
                else:
                    curr.left = NodeElement(new_data)
            elif new_data > curr.data:
                if curr.right:
                    curr = curr.right
                    self.insert(new_data, root=curr)
                else:
                    curr.right = NodeElement(new_data)
            else:  # Duplicate value
                curr.count += 1

    def print_inorder(self, node: NodeElement):
        if node:
            print(node.data)
            self.print_inorder(node=node.left)
            self.print_inorder(node=node.right)


if __name__ == '__main__':
    import random

    # random.seed(42)
    array = list(set([random.randint(0, 100) for _ in range(5)]))
    random.shuffle(array)
    print(array)
    bst = BST(array.pop(0))
    for element in array:
        bst.insert(element)
    bst.print_inorder()
