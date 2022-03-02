"""
Algorithm Preorder(tree)
   1. Visit the root.
   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
   3. Traverse the right subtree, i.e., call Preorder(right-subtree)

            1
          /   \
        2       3
      /   \
    4       5

Output: 1 2 4 5 3
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def print_preorder(node: Node) -> None:
    if node:
        # print the data of the node
        print(node.value)
        # Then recur the left child
        print_preorder(node.left)
        # Then recur the right child
        print_preorder(node.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_preorder(root)
