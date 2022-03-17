"""
Properties:
1. n - nodes => n - 1 edges
2. Tree is a recursive data structure
3. Degree of a node: Total number of children of a node.
4. Degree of a tree: Max(degree of all nodes)
5. Level: Number of generations
6. Height of a node: Number of edges from the Longest path from a leaf to that node.
7. Height of a tree: Height of the root node.
8. Depth of a node: Total number of edges from root to that node.
9. Depth of a tree: Total number of edges from root to the farthest leaf.

Types of Binary Trees:
1. Full Binary tree: Every non-leaf node has 2 children.
2. Complete Binary Tree: All the levels (except last) are completely filled. The last level leaf nodes are filled from
                         left to right
3. Perfect Binary Tree: All internal nodes contain 2 children and all leaf nodes are present of the same level.
4. Balanced Binary Tree: Difference of Heights of left sub-tree and right sub-tree is not greater than 1, for every node.
5. Pathological or Degenerate Binary Tree: Every parent has only 1 children.

Binary Search Tree or BST is a tree with following properties:
1. The left subtree of a node contains only nodes with keys lesser than node's key.
2. The right sub-tree of a node contains only nodes with keys greater than node's key.
3. The left sub-tree and right sub-tree must also be BST.

Application of trees:
1. Store hierarchical data, like folder structure, organization structure, XML/HTML data.
2. Binary Search Tree is a tree that allows fast search, insert, delete on a sorted data. It also allows finding closest item
3. Heap is a tree data structure which is implemented using arrays and used to implement priority queues.
4. B-Tree and B+ Tree : They are used to implement indexing in databases.
5. Syntax Tree:  Scanning, parsing , generation of code and evaluation of arithmetic expressions in Compiler design.
6. K-D Tree: A space partitioning tree used to organize points in K dimensional space.
7. Trie : Used to implement dictionaries with prefix lookup.
8. Suffix Tree : For quick pattern searching in a fixed text.
9. Spanning Trees and shortest path trees are used in routers and bridges respectively in computer networks
10. As a workflow for compositing digital images for visual effects.
11. Decision trees.
12. Organization chart of a large organization.

Tree traversals:
            1
          /   \
        2       3
      /   \
    4       5

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth-First or Level Order Traversal: 1 2 3 4 5

BSF vs DFS:
All four traversals require O(n) time as they visit every node exactly once.

Is there any difference in terms of Extra Space?
There is difference in terms of extra space required.

1. Extra Space required for Level Order Traversal is O(w) where w is maximum
width of Binary Tree. In level order traversal, queue one by one stores nodes
of different level.
2. Extra Space required for Depth First Traversals is O(h) where h is maximum
height of Binary Tree. In Depth First Traversals, stack (or function call stack)
stores all ancestors of a node.

Maximum Width of a Binary Tree at depth (or height) h can be 2h where h starts
from 0. So the maximum number of nodes can be at the last level. And worst case
occurs when Binary Tree is a perfect Binary Tree with numbers of nodes like
1, 3, 7, 15, …etc. In worst case, value of 2h is Ceil(n/2).

Height for a Balanced Binary Tree is O(Log n). Worst case occurs for skewed tree
and worst case height becomes O(n).

So in worst case extra space required is O(n) for both. But worst cases occur for
different types of trees.

It is evident from above points that extra space required for Level order traversal
is likely to be more when tree is more balanced and extra space for Depth First
Traversal is likely to be more when tree is less balanced.
"""
