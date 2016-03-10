# coding=utf-8
from dll import DoubleLink


class Queue(object):
    """Create a queue."""

    def __init__(self):
        """Initialize the queue."""
        self.head = None
        self.length = 0
        self.prev = None

    def enqueue(self, value):
        """Add a value to the queue."""
        self.queue = DoubleLink.insert(self, value)

    def dequeue(self):
        """Remove end item of queue and return the value."""
        deq_value = DoubleLink.shift(self)
        if deq_value is None:
            raise ValueError('Queue is empty')
        else:
            return deq_value

    def peek(self):
        """Return next value in queue without dequeueing."""
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            return current_node.value
        else:
            return None

    def size(self):
        """Return the length of the list."""
        return self.length
