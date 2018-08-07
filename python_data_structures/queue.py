"""Module to implement Queue in Python."""
from doubly_linked_list import DoublyLinkedList 


class Queue(object):
    """Class to create instance of Queue."""

    def __init__(self):
        """Create new instance of Queue class object."""
        self.queue = DoublyLinkedList()
        self.is_empty = True

    def enqueue(self, data):
        """Method to add given data to Queue class object."""
        self.queue.append(data)

    def dequeue(self):
        """Method to remove and return item at front of Queue class object."""
        self.queue.pop()

    def peek_front(self):
        """Method to return item at front of Queue class object."""
        return self.queue.head

    def peek_back(self):
        """Method to return item at back of Queue class object."""

