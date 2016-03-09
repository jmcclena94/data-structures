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
        x = self.head
        if x is not None:
            while x.next_node is not None:
                x = x.next_node
            new_node = Node(value)
            x.next_node = new_node
            new_node.prev = x

    def pop(self):
        pop_val = LinkedList.pop(self)
        return pop_val

    def shift(self):
        x = self.head
        if x is not None:
            while x.next_node is not None:
                x = x.next_node
            x.prev.next_node = None
            return x.value

    def remove(self, value):
        node_val = LinkedList.search(self, value)
        prev_node = node_val.prev
        next_node = node_val.next_node
        node_val.prev.next_node = next_node
        node_val.next_node.prev = prev_node
