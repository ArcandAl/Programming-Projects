### File: list_priority_queue.py

class ListPriorityQueue:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        #minItem = min(self._items)
        #minIndex = self._items.index(minItem)
        minIndex = 0
        for testIndex in range(1,len(self._items)):
            if self._items[testIndex] < self._items[minIndex]:
                minIndex = testIndex
        return self._items.pop(minIndex)

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        listCopy = [] + self._items
        listCopy.sort()
        return iter(listCopy)


if __name__ == '__main__':
    q = ListPriorityQueue()
    print("q.enqueue(5)")
    q.enqueue(5)
    print("q.enqueue(7)")
    q.enqueue(7)
    print("q.enqueue(3)")
    q.enqueue(3)
    print("q.enqueue(4)")
    q.enqueue(4)
    print(q)
    print("q.dequeue():",q.dequeue())
    print("q:",q)
    for item in q:
        print(item)
