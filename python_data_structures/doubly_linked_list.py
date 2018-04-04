"""Module to implement Doubly Linked List in Python."""


class Node(object):
    """Class to create instance of Node."""

    def __init__(self, data, next_node=None, prev_node=None):
        """Create new instance of Node class object."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList(object):
    """Class to create instance of Doubly Linked List."""

    def __init__(self):
        """Create new instance of DoublyLinkedList class object."""
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Method to add new Node to Doubly Linked List."""

        new_next_node = self.head
        self.head = Node(data, new_next_node)

        if not self.head.next_node:

            self.tail = self.head

        else:

            new_next_node.prev_node = self.head
