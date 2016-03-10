# coding=utf-8
from linked_list import LinkedList
from linked_list import Node


class DoubleLink(object):

    def __init__(self):
        self.prev = None
        self.head = None
        self.length = 0

    def insert(self, value):
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
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            new_node = Node(value)
            current_node.next_node = new_node
            new_node.prev = current_node

    def pop(self):
        pop_val = LinkedList.pop(self)
        return pop_val

    def shift(self):
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
        node_val = LinkedList.search(self, value)
        prev_node = node_val.prev
        next_node = node_val.next_node
        node_val.prev.next_node = next_node
        node_val.next_node.prev = prev_node
