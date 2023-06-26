class SortingStrategy:
    def sort(self, data):
        raise NotImplementedError()


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        # Implementation of Bubble Sort algorithm


class MergeSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Merge Sort")
        # Implementation of Merge Sort algorithm


class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        # Implementation of Quick Sort algorithm


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        self.strategy.sort(data)


# Usage
data = [5, 2, 8, 1, 9]

sorter = Sorter(BubbleSortStrategy())
sorter.sort_data(data)
# Output: Sorting using Bubble Sort

sorter.set_strategy(MergeSortStrategy())
sorter.sort_data(data)
# Output: Sorting using Merge Sort

sorter.set_strategy(QuickSortStrategy())
sorter.sort_data(data)
# Output: Sorting using Quick Sort
