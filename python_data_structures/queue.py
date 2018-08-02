"""Module to implement Queue in Python."""
from doubly_linked_list.py import DoublyLinkedList 


class Queue(object):
    """Class to create instance of Queue."""

    def __init__(self):
        """Create new instance of Queue class object."""
        self.queue = DoublyLinkedList()

