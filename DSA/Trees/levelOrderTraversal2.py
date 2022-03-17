"""
Method 2 (Using queue)

For each node, first the node is visited and then it’s child nodes are put in a
FIFO queue.

Algorithm:
printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children
      (first left then right children) to q
    c) Dequeue a node from q.
"""


class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_level_order(node: Node) -> None:
    if not node:
        return
    queue = [node]
    while len(queue) > 0:
        print(queue[0].data, end=" ")
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
print_level_order(root)
