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


def test_delete_node_method_returns_string_if_deleted_node_is_head():
    """Test that the delete_node method of the DoublyLinkedList class returns a
    specific string if Node to be deleted is the head of the list."""

    dll = DoublyLinkedList()
    dll.add_node(1)
    dll.add_node(2)

    assert dll.delete_node(2) == 'Node has been deleted.'


def test_delete_node_method_returns_string_if_deleted_node_is_found():
    """Test that the delete_node method of the DoublyLinkedList class returns a
    specific string if Node to be deleted is found and removed."""

    dll = DoublyLinkedList()
    dll.add_node(0)
    dll.add_node(5)
    dll.add_node(10)

    assert dll.delete_node(5) == 'Node has been deleted.'


def test_delete_node_method_returns_string_if_deleted_node_is_tail():
    """Test that the delete_node method of the DoublyLinkedList class returns a
    specific string if Node to be deleted is the tail of the list."""

    dll = DoublyLinkedList()
    dll.add_node(3)
    dll.add_node(6)

    assert dll.delete_node(3) == 'Node has been deleted.'


def test_delete_method_reassigns_head_and_tail_to_be_none_if_list_len_one():
    """Test that the delete_node method of the DoublyLinkedList class assigns
    the head and tail of the list to None if the list only has one Node."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    dll.delete_node(1)
    assert dll.head is None and dll.tail is None


def test_delete_node_method_removes_node_with_prev_and_next_pointers():
    """Test that the delete_node method of the DoublyLinkedList class
    successfully removes a Node with prev_node and next_node pointers actively
    pointing to other Nodes."""

    dll = DoublyLinkedList()

    for i in range(3):
        dll.add_node(i)

    dll.delete_node(2)
    assert dll.head.next_node.data != 2 and dll.tail.prev_node.data != 2


def test_delete_node_method_reassigns_head_to_be_next_node_if_deleting_head():
    """Test that the delete_node method of the DoublyLinkedList class correctly
    reassigns the list's head to be it's next_node if Node to be deleted is the
    list's head."""

    dll = DoublyLinkedList()
    dll.add_node(1)
    dll.add_node(2)

    dll.delete_node(2)
    assert dll.head.data == 1


def test_delete_node_method_reassigns_tail_to_be_prev_node_if_deleting_tail():
    """Test that the delete_node method of the DoublyLinkedList class correctly
    reassigns the list's tail to be it's prev_node if Node to be deleted is the
    list's tail."""

    dll = DoublyLinkedList()
    dll.add_node(30)
    dll.add_node(15)

    dll.delete_node(30)
    assert dll.tail.data == 15


def test_delete_method_raises_exception_if_list_is_empty():
    """Test that the delete_node method of the DoublyLinkedList class raises a
    LookupError if called on an empty list."""

    dll = DoublyLinkedList()

    with pytest.raises(LookupError):
        dll.delete_node(1)


def test_delete_method_raises_exception_if_node_not_found():
    """Test that the delete_node method of the DoublyLinkedList class raises a
    LookupError if a Node containing the given data is not found."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    with pytest.raises(LookupError):
        dll.delete_node(2)


def test_append_method_assigns_head_and_tail_to_be_same_node_if_list_empty():
    """Test that the append method of the DoublyLinkedList class correctly
    assigns the list's head and tail to be the same Node if append is used on
    an empty list."""

    dll = DoublyLinkedList()
    dll.append(1)

    assert dll.tail is dll.head


def test_append_method_correctly_reassigns_tail_to_newly_added_node():
    """Test that the append method of the DoublyLinkedList class correctly
    reassigns the list's tail to become the newly appended Node."""

    dll = DoublyLinkedList()
    dll.add_node(1)
    old_tail = dll.tail

    dll.append(2)
    assert dll.tail != old_tail and dll.tail.data != old_tail.data


def test_append_method_assigns_old_tails_next_node_to_be_new_tail():
    """Test that the append method of the DoublyLinkedList class assigns the
    old tail's next_node pointer to be the new tail, preserving the integrity
    of the list."""

    dll = DoublyLinkedList()
    dll.add_node(0)
    old_tail = dll.tail

    dll.append(5)
    assert old_tail.next_node is dll.tail


def test_append_method_assigns_new_tails_prev_node_to_be_old_tail():
    """Test that the append method of the DoublyLinkedList class assigns the
    new tail's prev_node pointer to be the old tail, preserving the integrity
    of the list."""

    dll = DoublyLinkedList()
    dll.add_node(10)
    old_tail = dll.tail

    dll.append(20)
    assert dll.tail.prev_node is old_tail


def test_append_method_creates_instance_of_node_class_as_new_node():
    """Test that the append method of the DoublyLinkedList class adds an
    instance of the Node class as the new Node in the list."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    dll.append(2)
    assert isinstance(dll.tail, Node)


def test_append_method_does_not_reassign_head_through_multiple_uses():
    """Test that the append method of the DoublyLinkedList class doesn't
    reassign the list's head after first use, even after multiple uses."""

    dll = DoublyLinkedList()
    dll.append(5)

    head = dll.head

    dll.append(10)
    dll.append(15)

    assert dll.head is head


def test_append_method_correctly_reassigns_tail_through_multiple_uses():
    """Test that the append method of the DoublyLinkedList class correctly
    reassigns the list's tail after multiple uses."""

    dll = DoublyLinkedList()
    dll.append(3)

    old_tail = dll.tail

    dll.append(6)
    dll.append(9)

    assert dll.tail is not old_tail


def test_shift_method_raises_exception_if_list_is_empty():
    """Test that the shift method of the DoublyLinkedList class raises an
    IndexError if the list is empty."""

    dll = DoublyLinkedList()

    with pytest.raises(IndexError):
        dll.shift()


def test_shift_method_assigns_head_node_to_none_if_list_length_is_one():
    """Test that the shift method of the DoublyLinkedList class assigns the
    head Node to become None if the list only contains one Node."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    dll.shift()
    assert dll.head is None


def test_shift_method_assigns_tail_node_to_none_if_list_length_is_one():
    """Test that the shift method of the DoublyLinkedList class assigns the
    tail Node to become None if the list only contains one Node."""

    dll = DoublyLinkedList()
    dll.add_node(1)

    dll.shift()
    assert dll.tail is None


def test_shift_method_returns_tail_node_data():
    """Test that the shift method of the DoublyLinkedList class returns the
    tail Node's data."""

    dll = DoublyLinkedList()
    dll.add_node(5)

    assert dll.shift() == 5
