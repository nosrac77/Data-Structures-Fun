"""Module to implement Doubly Linked List in Python."""


class Node(object):
    """Class to create instance of Node."""

    def __init__(self, data, next_node, prev_node):
        """Create new instance of Node class object."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList(object):
    """Class to create instance of Doubly Linked List."""

    def __init__(self, head, tail):
        """Create new instance of DoublyLinkedList class object."""
        self.head = head
        self.tail = tail
