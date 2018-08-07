"""Module containing pytest tests for Queue."""

from doubly_linked_list import DoublyLinkedList
from queue import Queue
import pytest


def test_new_queue_attribute_queue_is_instance_of_doubly_linked_list():
    """Test that a newly created Queue class object has an attribute queue
    that is an instance of the Doubly Linked List class."""

    queue = Queue()
    assert isinstance(queue.queue, DoublyLinkedList)
