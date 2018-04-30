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
