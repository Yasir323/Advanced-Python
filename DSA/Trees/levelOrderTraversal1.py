"""
Method 1 (Use function to print a current level)

There are basically two functions in this method. One is to print all nodes at a
given level (printCurrentLevel), and other is to print level order traversal of
the tree (printLevelorder). printLevelorder makes use of printCurrentLevel to
print nodes at all levels one by one starting from the root.
Algorithm:
/*Function to print level order traversal of tree*/
printLevelorder(tree)
for d = 1 to height(tree)
   printCurrentLevel(tree, d);

/*Function to print all nodes at a current level*/
printCurrentLevel(tree, level)
if tree is NULL then return;
if level is 1, then
    print(tree->data);
else if level greater than 1, then
    printCurrentLevel(tree->left, level-1);
    printCurrentLevel(tree->right, level-1);
"""


class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def height(node: Node) -> int:
    if not node:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        # Use the larger one
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


def print_current_level(node: Node, level: int) -> None:
    if not node:
        return
    if level == 1:
        print(node.data, end=" ")
    elif level > 1:
        print_current_level(node.left, level - 1)
        print_current_level(node.right, level - 1)


def print_level_order(node: Node) -> None:
    h = height(node)
    for i in range(1, h + 1):
        print_current_level(node, i)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
print_level_order(root)
