"""Module containing pytest tests for Queue."""

from doubly_linked_list import DoublyLinkedList
from queue import Queue
import pytest


def test_new_queue_attribute_queue_is_instance_of_doubly_linked_list():
    """Test that a newly created Queue class object has an attribute queue
    that is an instance of the Doubly Linked List class."""

    queue = Queue()
    assert isinstance(queue.queue, DoublyLinkedList)


def test_new_queue_attribute_is_empty_is_true():
    """Test that a newly created Queue class object has an attribute is_empty
    that is True."""

    queue = Queue()
    assert queue.is_empty is True


def test_enqueue_method_sets_is_empty_attribute_to_false():
    """Test that the enqueue method of the Queue class object sets the
    is_empty attribute to False."""

    queue = Queue()
    queue.enqueue(1)
    assert queue.is_empty is False

