# coding=utf-8
from linked_list import LinkedList
# from linked_list import Node


class Stack(object):
    """Create a new Stack."""

    def __init__(self, value):
        """Initialize the stack."""
        self.head = None
        self.length = 0
        self.stack = LinkedList()
        self.stack.insert(value)

    def push(self, value):
        """Push a new value onto the stack."""
        self.stack.insert(value)

    def pop(self):
        """Remove the first value on the stack."""
        pop_val = self.stack.pop()
        return pop_val
