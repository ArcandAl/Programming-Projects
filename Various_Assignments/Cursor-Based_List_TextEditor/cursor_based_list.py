"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  Alec Arcand
"""

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""

    def __init__(self):
        """ Creates an empty cursor-based list."""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getPrevious() != self._header

    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        self._current = self._header.getNext()

    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        self._current = self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if self.hasNext():
            self._current = self._current.getNext()

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one item"""
        if self.hasPrevious():
            self._current = self._current.getPrevious()

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        temp = Node2Way(item)
        if self.isEmpty():
            temp.setNext(self._trailer)
            temp.setPrevious(self._header)
            self._trailer.setPrevious(temp)
            self._header.setNext(temp)
        else:
            temp.setNext(self._current.getNext())
            self._current.getNext().setPrevious(temp)
            self._current.setNext(temp)
            temp.setPrevious(self._current)
        self._current = temp
        self._size += 1

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        temp = Node2Way(item)
        if self.isEmpty():
            temp.setPrevious(self._header)
            temp.setNext(self._trailer)
            self._header.setNext(temp)
            self._trailer.setPrevious(temp)
        else:
            temp.setNext(self._current)
            self._current.getPrevious().setNext(temp)
            temp.setPrevious(self._current.getPrevious())
            self._current.setPrevious(temp)
        self._current = temp
        self._size += 1

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        temp = self._current
        if temp == self._trailer:
            return self._trailer.getData()
        else:
            self._current.getPrevious().setNext(self._current.getNext())
            self._current.getNext().setPrevious(self._current.getPrevious())
            if self._current.getNext() == self._trailer:
                self._current = self._current.getPrevious()
            else:
                self._current = self._current.getNext()
            self._size -= 1
        return temp.getData()


    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        temp = Node2Way(newItemValue)
        temp.setNext(self._current.getNext())
        temp.setPrevious(self._current.getPrevious())
        self._current.getNext().setPrevious(temp)
        self._current.getPrevious().setNext(temp)
        self._current = temp

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        """ Returns the number of items in the list."""
        # replace below
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        # replace below
        stackStr = ""

        current = self._header
        while current != None:
            stackStr += str(current.getData()) + " "
            current = current.getNext()

        return stackStr
