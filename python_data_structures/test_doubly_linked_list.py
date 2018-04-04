"""Module containing pytest tests for Doubly Linked List."""

from doubly_linked_list import DoublyLinkedList, Node


def test_add_node_method_adds_instance_of_node_to_list():
    """Test that the add_node method of the DoublyLinkedList class adds an
    instance of the Node class to the list."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    assert isinstance(dll.head, Node)


def test_add_node_method_adds_node_containing_given_data_to_list():
    """Test that the add_node method of the DoublyLinkedList class adds a Node
    containing the given data to the list."""

    dll = DoublyLinkedList()
    dll.add_node(5)

    assert dll.head.data == 5


def test_add_node_method_reassigns_head_and_tail_to_same_node_if_list_empty():
    """Test that the add_node method of the DoublyLinkedList class reassigns
    the head and tail of the list to become the same Node if the list being
    added to is empty."""

    dll = DoublyLinkedList()
    dll.add_node(3)

    assert dll.head is dll.tail
