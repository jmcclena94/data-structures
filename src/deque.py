# coding=utf-8
from dll import DoubleLink
from queue import Queue


class Node(object):
    """Create a deque node."""

    def __init__(self, value):
        """Initialize the list node."""
        self.value = value
        self.next_node = None


class Deque(object):
    """Create a Deque object."""

    def __init__(self):
        """Initialize the deque."""
        self.head = None
        self.length = 0
        self.prev = None

    def append(self, value):
        """Append a value to the end of the deque."""
        current_node = self.head
        self.length += 1
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            new_node = Node(value)
            current_node.next_node = new_node
            new_node.prev = current_node
        else:
            new_node = Node(value)
            current_node = new_node
            self.head = current_node

    def appendleft(self, value):
        """Append a value to the start of the deque."""
        self.deque = DoubleLink.insert(self, value)

    def pop(self):
        """Remove a value from the end of the deque and return it."""
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            if current_node == self.head:
                self.head = None
            self.length -= 1
            return current_node.value
        else:
            try:
                current_node.prev.next_node = None
            except AttributeError:
                print('The Deque is empty')
                raise AttributeError

    def popleft(self):
        """Remove a value from the start of the deque and return it."""
        try:
            pop_val = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            return pop_val
        except AttributeError:
            print('The Deque is empty')
            raise AttributeError

    def peek(self):
        return Queue.peek(self)

    def peekleft(self):
        return self.head.value

    def size(self):
        return self.length
