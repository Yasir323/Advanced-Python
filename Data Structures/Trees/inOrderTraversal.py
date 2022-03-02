"""
Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)

            1
          /   \
        2       3
      /   \
    4       5

Output: 4 2 5 1 3
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def print_inorder(node: Node) -> None:
    if node:
        # First recur the left child
        print_inorder(node.left)
        # Then print the data of the node
        print(node.value)
        # Then recur the right child
        print_inorder(node.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_inorder(root)
