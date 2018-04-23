"""Module containing pytest tests for Doubly Linked List."""

from doubly_linked_list import DoublyLinkedList, Node
import pytest


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


def test_add_node_method_reassigns_tail_to_always_be_first_node_added():
    """Test that the add_node method of the DoublyLinkedList class maintains
    the tail of the list properly, ensuring that no matter how many Nodes are
    added that the tail is always the first Node that was added to the list."""

    dll = DoublyLinkedList()

    for i in range(5):
        dll.add_node(i)

    assert dll.tail.data == 0


def test_add_node_method_properly_assigns_next_node_pointer():
    """Test that the add_node method of the DoublyLinkedList accurately assigns
    the next_node pointer to be the next Node in the list."""

    dll = DoublyLinkedList()
    dll.add_node(1)
    dll.add_node(2)

    assert dll.head.next_node.data == 1


def test_add_node_method_properly_assigns_prev_node_pointer():
    """Test that the add_node method of the DoublyLinkedList class accurately
    assigns the prev_node pointer to be the previous Node in the list."""

    dll = DoublyLinkedList()
    dll.add_node(10)
    dll.add_node(20)

    assert dll.tail.prev_node.data == 20


def test_pop_method_raises_exception_if_list_is_empty():
    """Test that the pop method of the DoublyLinkedList class raises an
    IndexError if the list is empty."""

    dll = DoublyLinkedList()

    with pytest.raises(IndexError):
        dll.pop()


def test_pop_method_reassigns_head_to_become_none_if_list_length_is_one():
    """Test that the pop method of the DoublyLinkedList class reassigns the
    list's head to become None if the list only contains one Node."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    dll.pop()
    assert dll.head is None


def test_pop_method_reassigns_tail_to_become_none_if_list_length_is_one():
    """Test that the pop method of the DoublyLinkedList class reassigns the
    list's tail to become None if the list only contains one Node."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    dll.pop()
    assert dll.tail is None


def test_pop_method_returns_data_in_old_head_node():
    """Test that the pop method of the DoublyLinkedList class returns the data
    contained in the old head Node."""

    dll = DoublyLinkedList()
    dll.add_node(5)

    assert dll.pop() == 5


def test_pop_method_reassigns_head_to_become_next_node():
    """Test that the pop method of the DoublyLinkedList class correctly
    reassigns the head to become it's next_node if the list contains more than
    one Node."""

    dll = DoublyLinkedList()
    dll.add_node(3)
    dll.add_node(6)

    head_next_node = dll.head.next_node
    dll.pop()
    assert dll.head is head_next_node


def test_pop_method_newly_reassigned_head_prev_node_is_none():
    """Test that the pop method of the DoublyLinkedList class assigns the
    prev_node pointer of the newly reassigned head to be None."""

    dll = DoublyLinkedList()
    dll.add_node(5)
    dll.add_node(10)

    dll.pop()
    assert dll.head.prev_node is None


def test_pop_method_correctly_reassigns_head_and_returns_data_multiple_uses():
    """Test that the pop method of the DoublyLinkedList class correctly
    reassigns the head and returns the old head's data after multiple uses."""

    dll = DoublyLinkedList()

    for num in range(10):
        dll.add_node(num)

    for _ in range(10):
        old_head = dll.head
        assert dll.pop() == old_head.data and dll.head is not old_head
