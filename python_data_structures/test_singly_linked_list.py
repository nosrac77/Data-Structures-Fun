"""Module containing pytest tests for the Singly Linked List."""
from singly_linked_list import Node, SinglyLinkedList


def test_new_node_instance_has_data_equal_to_None():
    """Test that a newly created instance of the Node class has data equal
    to None."""

    new_node = Node()
    assert new_node.data is None


def test_new_node_instance_has_next_node_equal_to_None():
    """Test that a newly created instance of the Node class has next_node equal
    to None."""

    new_node = Node()
    assert new_node.next_node is None


def test_new_instance_of_node_accepts_param_arguments():
    """Test that a newly created instance of the Node class accepts arguments
    and places values in appropriate attributes."""

    new_node = Node('data value', 'next_node value')
    assert new_node.data == 'data value'
    assert new_node.next_node == 'next_node value'


def test_slfjdklfjadskljfldskafs():
    """."""

    ll = SinglyLinkedList()
