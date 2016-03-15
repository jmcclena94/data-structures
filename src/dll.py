# coding=utf-8
from linked_list import LinkedList
from linked_list import Node


class DoubleLink(object):
    """Create a double linked list."""

    def __init__(self):
        """Initialize the double linked list."""
        self.prev = None
        self.head = None
        self.length = 0
        self.linked_list = LinkedList()

    def insert(self, value):
        """Insert a value onto the double linked list."""
        try:
            for i in value:
                new_node_value = Node(i)
                if self.head is None:
                    self.head = new_node_value
                    self.length += 1
                else:
                    new_node_value.next_node = self.head
                    new_node_value.next_node.prev = new_node_value
                    self.head = new_node_value
                    self.length += 1
        except TypeError:
            new_node_value = Node(value)
            if self.head is None:
                self.head = new_node_value
                self.length += 1
            else:
                new_node_value.next_node = self.head
                new_node_value.next_node.prev = new_node_value
                self.head = new_node_value
                self.length += 1

    def append(self, value):
        """Append a value to the end of a double link list."""
        current_node = self.head
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

    def pop(self):
        """Remove the first value of the list."""
        pop_value = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return pop_value

    def shift(self):
        """Remove the last value of the list."""
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            try:
                current_node.prev.next_node = None
            except AttributeError:
                current_node.next_node = None
                self.head = None
            return current_node.value

    def remove(self, value):
        """Remove a specified value from the list."""
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                if (current_node.value == value):
                    node_val = current_node
                current_node = current_node.next_node
            if (current_node.value == value):
                node_val = current_node
        prev_node = node_val.prev
        next_node = node_val.next_node
        node_val.prev.next_node = next_node
        node_val.next_node.prev = prev_node
