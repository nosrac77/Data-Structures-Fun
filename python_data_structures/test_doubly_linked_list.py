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
