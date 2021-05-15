""" File: reverse_sorted_list_priority_queue.py
    Description:  Priority queue implemented using a Python list ordered by
    priority in ascending order.
"""


class ReverseSortedListPriorityQueue:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        testIndex = len(self._items) - 1
        self._items.append(item)
        while testIndex >= 0 and item < self._items[testIndex]:
            self._items[testIndex + 1] = self._items[testIndex]
            testIndex -= 1
        self._items[testIndex+1] = item

    def dequeue(self):
        retValue = self._items[0]
        for index in range(len(self._items)-1):
            self._items[index] = self._items[index+1]
        self._items.pop()
        return retValue

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        currentIndex =  0
        while currentIndex < len(self._items):
            yield self._items[currentIndex]
            currentIndex += 1
        raise StopIteration
