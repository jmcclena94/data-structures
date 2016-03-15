# coding=utf-8
from dll import DoubleLink


class Deque_Node(object):
    """Create a deque node."""

    def __init__(self, value):
        """Initialize the list node."""
        self.value = value
        self.next_node = None


class Deque(object):
    """Create a Deque object."""

    def __init__(self):
        """Initialize the deque."""
        self.container = DoubleLink()
        self.container.head = None
        self.length = 0
        self.container.prev = None

    def append(self, value):
        """Append a value to the end of the deque."""
        current_node = self.container.head
        self.length += 1
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            new_node = Deque_Node(value)
            current_node.next_node = new_node
            new_node.prev = current_node
        else:
            new_node = Deque_Node(value)
            current_node = new_node
            self.container.head = current_node

    def appendleft(self, value):
        """Append a value to the start of the deque."""
        self.container.insert(value)

    def pop(self):
        """Remove a value from the end of the deque and return it."""
        current_node = self.container.head
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            if current_node == self.container.head:
                self.container.head = None
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
            pop_val = self.container.head.value
            self.container.head = self.container.head.next_node
            self.length -= 1
            return pop_val
        except AttributeError:
            print('The Deque is empty')
            raise AttributeError

    def peek(self):
        current_node = self.container.head
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            return current_node.value
        else:
            return None

    def peekleft(self):
        return self.container.head.value

    def size(self):
        return self.container.length
