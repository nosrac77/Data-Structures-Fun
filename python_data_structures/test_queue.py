"""Module containing pytest tests for Queue in Python."""

from doubly_linked_list import DoublyLinkedList
from queue import Queue


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


def test_enqueue_method_changes_is_empty_attribute_to_false_if_empty_queue():
    """Test that the enqueue method of the Queue class object changes the
    is_empty attribute from True to False if used on empty Queue."""

    queue = Queue()
    assert queue.is_empty is True
    queue.enqueue(1)
    assert queue.is_empty is False


def test_enqueue_method_adds_item_with_given_data_to_queue():
    """Test that the enqueue method of the Queue class object adds an item to
    the queue with the given data."""

    queue = Queue()
    queue.enqueue(1)
    assert queue.queue.head.data == 1


def test_enqueue_method_changes_queue_head_from_none_to_added_data():
    """Test that the enqueue method of the Queue class object changes the value
    of the Queue's head from None to the data added."""

    queue = Queue()
    assert queue.queue.head is None
    queue.enqueue(5)
    assert queue.queue.head and queue.queue.head.data == 5


def test_enqueue_method_changes_queue_tail_from_none_to_added_data():
    """Test that the enqueue method of the Queue class object changes the value
    of the Queue's tail from None to the data added."""

    queue = Queue()
    assert queue.queue.tail is None
    queue.enqueue(5)
    assert queue.queue.tail and queue.queue.tail.data == 5


def test_enqueue_method_always_adds_items_to_rear_of_queue():
    """Test that the enqueue method of the Queue class object always adds
    items to the rear of the queue, replacing the old rear with the newest
    added item."""

    queue = Queue()
    queue.enqueue(1)
    old_rear_of_queue = queue.queue.tail.data
    queue.enqueue(2)
    new_rear_of_queue = queue.queue.tail.data

    assert old_rear_of_queue != new_rear_of_queue


def test_enqueue_method_does_not_add_items_to_front_of_queue():
    """Test that the enqueue method of the Queue class object does not add
    items to the front of the queue."""

    queue = Queue()
    queue.enqueue(5)
    queue_front_item = queue.queue.head.data
    queue.enqueue(10)

    assert queue.queue.head.data == queue_front_item


def test_dequeue_method_sets_is_empty_attribute_to_true_if_queue_empty():
    """Test that the dequeue method of the Queue class object sets the is_empty
    attribute to True if the Queue is rendered empty as a result of the
    method's use."""

    queue = Queue()
    queue.enqueue(1)
    queue.dequeue()

    assert queue.is_empty is True

