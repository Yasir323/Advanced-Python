"""The Iterator pattern is commonly used when you have a custom collection or data structure and you want to provide
a way to iterate over its elements without exposing its underlying implementation. """


class CustomCollection:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def __iter__(self):
        return CustomIterator(self.data)


class CustomIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        item = self.collection[self.index]
        self.index += 1
        return item


# Usage
collection = CustomCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

for item in collection:
    print(item)
