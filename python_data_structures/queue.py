"""Module to implement Queue in Python."""
from doubly_linked_list.py import DoublyLinkedList 


class Queue(object):
    """Class to create instance of Queue."""

    def __init__(self):
        """Create new instance of Queue class object."""
        self.queue = DoublyLinkedList()
        self.is_empty = True

    def enqueue(self, data):
        """Method to add given data to Queue class Object."""
       self.queue.append(data)

    def dequeue(self):
        """Method to remove."""

