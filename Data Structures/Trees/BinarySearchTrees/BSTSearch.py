class EmptyTreeError(Exception):
    """Raised when tree is empty."""

    def __init__(self, message="Tree is empty") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_empty(self):
        if self.data is None:
            return True
        else:
            return False

    def insert(self, new_data):
        if self.data is None:
            self.data = new_data
            return
        if self.data == new_data:
            return
        if new_data < self.data:
            if self.left:
                self.left.insert(new_data)
            else:
                self.left = BST(new_data)
        else:
            if self.right:
                self.right.insert(new_data)
            else:
                self.right = BST(new_data)

    def print_preorder(self):
        """In-order traversal of BST."""
        print(self.data, end=' ')
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def search(self, data):
        if self.data:
            if self.data == data:
                print('Found!')
                return
            elif data < self.data:
                # Look to the left
                if self.left:
                    self.left.search(data)
                else:
                    print('Not Found!')
            else:
                # Look to the right
                if self.right:
                    self.right.search(data)
                else:
                    print('Not Found!')


if __name__ == '__main__':
    import random

    # random.seed(42)
    array = list(set([random.randint(30, 40) for _ in range(5)]))
    random.shuffle(array)
    print(array)
    bst = BST(350)
    for element in array:
        bst.insert(element)
    bst.print_preorder()
    print()
    # Search
    bst.search(36)
