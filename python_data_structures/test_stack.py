"""Module containing tests for Stack implementation in Python."""

from stack import Stack
import pytest


def test_newly_initialized_stack_is_empty_attribute_set_to_equal_true():
    """Test that the is_empty attribute on a newly initialized Stack class
    object is set to equal True."""

    stack = Stack()
    assert stack.is_empty is True


def test_newly_initialized_stack_stack_attribute_equals_empty_list():
    """Test that the stack attribute on a newly initialized Stack class object
    equals an empty list."""

    stack = Stack()
    assert stack.stack == []


def test_newly_initialized_stack_top_attribute_equals_none():
    """Test that the top attribute on a newly initialized Stack class object
    equals None."""

    stack = Stack()
    assert stack.top is None


def test_push_method_adds_given_data_to_stack_list():
    """Test that the push method of the Stack class object adds the given
    data to the Stack's stack list."""

    stack = Stack()
    stack.push(1)

    assert 1 in stack.stack


def test_push_method_adds_given_data_to_index_zero_of_stack_list():
    """Test that the push method of the Stack class object adds the given
    data to the Stack's stack list at index zero."""

    stack = Stack()
    stack.push(5)

    assert stack.stack[-1] == 5


def test_push_method_assigns_stack_top_to_newly_added_data():
    """Test that the push method of the Stack class object assigns the stack's
    top attribute to equal the newly added data."""

    stack = Stack()
    stack.push(10)

    assert stack.top == 10


def test_push_method_assigns_stack_top_to_equal_stack_list_at_index_zero():
    """Test that the push method of the Stack class object assigns the stack's
    top attribute to equal the data contained at index zero of the Stack's
    stack list."""

    stack = Stack()
    stack.push(3)

    assert stack.top == stack.stack[-1]


def test_push_method_correctly_reassigns_stack_top_through_multiple_pushes():
    """Test that the push method of the Stack class object correctly reassigns
    the Stack's top through multiple calls of the push method."""

    stack = Stack()

    for data in range(10):
        stack.push(data)
        assert stack.top == data and stack.stack[-1] == data


def test_push_method_sets_is_empty_attribute_to_false():
    """Test that the push method of the Stack class object sets the is_empty
    attribute to False."""

    stack = Stack()
    stack.push(1)

    assert stack.is_empty is False


def test_pop_from_stack_method_returns_stack_top_data():
    """Test that the pop_from_stack method of the Stack class object returns
    the data of the Stack's top."""

    stack = Stack()
    stack.push(1)

    stack_top = stack.top
    assert stack.pop_from_stack() == stack_top


def test_pop_from_stack_method_returns_stack_list_at_index_negative_one():
    """Test that the pop_from_stack method of the Stack class object returns
    the element of the Stack's stack list at the index of negative one."""

    stack = Stack()
    stack.push(1)

    data_at_index_negative_one = stack.stack[-1]
    assert stack.pop_from_stack() == data_at_index_negative_one


def test_pop_from_stack_method_raises_exception_if_stack_is_empty():
    """Test that the pop_from_stack method of the Stack class object raises an
    IndexError if the Stack is empty."""

    stack = Stack()

    with pytest.raises(IndexError):
        stack.pop_from_stack()


def test_pop_from_stack_method_sets_is_empty_to_true_if_stack_len_is_one():
    """Test that the pop_from_stack method of the Stack class object sets the
    Stack's is_empty attribute to True if the Stack only contains one item
    (rendering the Stack empty after the pop_from_stack method is called)."""

    stack = Stack()
    stack.push(5)

    stack.pop_from_stack()
    assert stack.is_empty is True
