"""Module containing pytest tests for Doubly Linked List."""

from doubly_linked_list import DoublyLinkedList, Node


def test_add_node_method_adds_instance_of_node_to_list():
    """Test that the add_node method of the DoublyLinkedList class adds an
    instance of the Node class to the list."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    assert isinstance(dll.head, Node)
