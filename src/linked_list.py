# coding=utf-8


class Node(object):
    """Create a list node."""

    def __init__(self, value):
        """Initialize the list node."""
        self.value = value
        self.next_node = None


class LinkedList(object):
    """Create a linked list."""

    def __init__(self):
        """Initialize a linked list."""
        self.head = None
        self.length = 0

    def insert(self, value):
        """Insert a value to the list."""
        try:
            for i in value:
                new_node_value = Node(i)
                if self.head is None:
                    self.head = new_node_value
                    self.length += 1
                else:
                    new_node_value.next_node = self.head
                    self.head = new_node_value
                    self.length += 1
        except TypeError:
            new_node_value = Node(value)
            if self.head is None:
                self.head = new_node_value
                self.length += 1
            else:
                new_node_value.next_node = self.head
                self.head = new_node_value
                self.length += 1

    def pop(self):
        """Remove the head of the list."""
        pop_value = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return pop_value

    def size(self):
        """Return the size of the list."""
        return self.length

    def search(self, value):
        """Search for a value in the list."""
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                if (current_node.value == value):
                    return current_node
                current_node = current_node.next_node
            if (current_node.value == value):
                return current_node

    def remove(self, value):
        """Remove a value from the list."""
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                if (current_node.next_node.value == value):
                    current_node.next_node = current_node.next_node.next_node
                    self.length -= 1
                current_node = current_node.next_node

    def display(self):
        """Display the list."""
        tup = []
        current_node = self.head
        while current_node is not None:
            tup.append(current_node.value)
            current_node = current_node.next_node
        tup = tuple(tup)
        print(tup)
        return tup
