"""Module to implement Singly Linked List in Python."""


class Node(object):
    """Class to create instance of Node."""

    def __init__(self, data=None, next_node=None):
        """Create new intance of a Node class object."""

        self.data = data
        self.next_node = next_node


class SinglyLinkedList(object):
    """Class to create instance of Singly Linked List."""

    def __init__(self):
        """Create new instance of a Singly Linked List class object."""

        self.head = Node()
        self.next_node = None

    def add_node(self, data):
        """Method to add new Node to Singly Linked List."""

        if self.head:
            new_next_node = self.head
            self.head = Node(data, new_next_node)
        else:
            self.head = Node(data)
