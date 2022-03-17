"""
Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.

            1
          /   \
        2       3
      /   \
    4       5

Output: 4 5 2 3 1
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def print_postorder(node: Node) -> None:
    if node:
        # First recur the left child
        print_postorder(node.left)
        # Then recur the right child
        print_postorder(node.right)
        # Then print the data of the node
        print(node.value)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_postorder(root)
"""
Time Complexity: O(n) 
Let us see different corner cases. 
Complexity function T(n) — for all problems where tree traversal is involved — can be defined as:
T(n) = T(k) + T(n – k – 1) + c
Where k is the number of nodes on one side of the root and n-k-1 on the other side.
Let’s do an analysis of boundary conditions
Case 1: Skewed tree (One of the subtrees is empty and another subtree is non-empty )
k is 0 in this case. 
T(n) = T(0) + T(n-1) + c 
T(n) = 2T(0) + T(n-2) + 2c 
T(n) = 3T(0) + T(n-3) + 3c 
T(n) = 4T(0) + T(n-4) + 4c
………………………………………… 
…………………………………………. 
T(n) = (n-1)T(0) + T(1) + (n-1)c 
T(n) = nT(0) + (n)c
Value of T(0) will be some constant say d. (traversing an empty tree will take some constants time)
T(n) = n(c+d) 
T(n) = Θ(n) (Theta of n)
Case 2: Both left and right subtrees have an equal number of nodes.
T(n) = 2T(|_n/2_|) + c
This recursive function is in the standard form (T(n) = aT(n/b) + (-)(n) ) for master method . 
If we solve it by master method we get (-)(n)
"""
