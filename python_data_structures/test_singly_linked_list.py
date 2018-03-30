"""Module containing pytest tests for the Singly Linked List."""
from singly_linked_list import Node, SinglyLinkedList
import pytest


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


def test_new_singly_linked_list_instance_has_head_equal_to_none():
    """Test that a newly created instance of the SinglyLinkedList class is
    initialized with a head attribute equal to None."""

    ll = SinglyLinkedList()
    assert ll.head is None


def test_add_node_method_adds_new_Node_class_to_Singly_Linked_Class():
    """Test that the add_node method of the Singly Linked List class
    successfully adds a new instance of the Node class."""

    ll = SinglyLinkedList()
    ll.add_node(1)
    assert isinstance(ll.head, Node)


def test_add_node_method_replaces_None_value_in_head_with_Node_object():
    """Test that the add_node method of the Singly Linked List class replaces
    the value of None in an empty list's head attribute with the Node class
    object."""

    ll = SinglyLinkedList()
    ll.add_node(1)
    assert ll.head is not None
    assert hasattr(ll.head, 'data') and hasattr(ll.head, 'next_node')


def test_add_node_method_replaces_head_when_multiple_nodes_added():
    """Test that the add_node method of the Singly Linked List class
    consistently replaces the head of the list with the newest added Node."""

    ll = SinglyLinkedList()

    for i in range(5):
        ll.add_node(i)
        assert ll.head.data == i


def test_delete_node_method_removes_node_with_given_data():
    """Test that the delete_node method of the Singly Linked List class
    removes a Node from the list with the given data."""

    ll = SinglyLinkedList()
    ll.add_node(1)
    ll.delete_node(1)

    assert ll.head is None


def test_delete_node_raises_exception_if_node_with_given_data_not_in_list():
    """Test that the delete_node method of the Singly Linked List class raises
    an exception if no Node with the given data exists in the list."""

    ll = SinglyLinkedList()
    ll.add_node(1)

    with pytest.raises(LookupError):
        assert ll.delete_node(5)


def test_delete_node_method_raises_exception_if_list_is_empty():
    """Test that the delete_node method of the Singly Linked List class raises
    an exception if used on an empty list."""

    ll = SinglyLinkedList()

    with pytest.raises(LookupError):
        assert ll.delete_node(1)


def test_delete_node_method_reassigns_head_of_list_if_head_is_deleted():
    """Test that the delete_node method of the Singly Linked List class
    correctly reassigns the head Node of the list to the next Node if the head
    Node is removed."""

    ll = SinglyLinkedList()
    ll.add_node(1)
    ll.add_node(2)

    ll.delete_node(2)
    assert ll.head.data == 1


def test_delete_node_method_reassigns_next_node_to_none_if_deleting_end_Node():
    """Test that the delete_node method of the Singly Linked List correctly
    reassigns the next_node to Node if it's removing the last Node of the list
    ."""

    ll = SinglyLinkedList()
    ll.add_node(1)
    ll.add_node(2)

    ll.delete_node(1)
    assert ll.head.next_node is None


def test_delete_node_method_correctly_reassigns_pointers_if_deleting_middle():
    """Test that the delete_node method of the Singly Linked List class
    correctly reassigns pointers if deleting a Node that has two Nodes on
    either side of it."""

    ll = SinglyLinkedList()

    for i in range(3):
        ll.add_node(i)

    ll.delete_node(1)
    assert ll.head.data == 2 and ll.head.next_node.data == 0


def test_delete_node_method_returns_data_value_of_deleted_node():
    """Test that the delete_node method of the Singly Linked List class returns
    the data value of the Node that it deletes."""

    ll = SinglyLinkedList()
    ll.add_node(1)

    assert ll.delete_node(1) == 1


def test_search_method_returns_node_if_node_containing_data_exists_in_list():
    """Test that the search method of the Singly Linked List class returns Node
    containing given data if it exists in the list."""

    ll = SinglyLinkedList()
    ll.add_node(1)

    assert ll.search(1) is ll.head


def test_search_method_raises_exception_if_node_containing_data_absent():
    """Test that the search method of the Singly Linked List class raises a
    LookupError if no Node in list contains given data."""

    ll = SinglyLinkedList()
    ll.add_node(1)

    with pytest.raises(LookupError):
        assert ll.search(5)


def test_search_method_raises_exception_if_list_is_empty():
    """Test that the search method of the Singly Linked List class raises a
    LookupError if the list is empty."""

    ll = SinglyLinkedList()

    with pytest.raises(LookupError):
        assert ll.search(1)
