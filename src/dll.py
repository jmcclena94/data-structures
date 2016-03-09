# coding=utf-8
from linked_list import LinkedList
from linked_list import Node


class DoubleLink(object):

    def __init__(self, value):
        self.head = None
        self.length = 0
        self.dll = LinkedList.insert(self, value)

    def insert(self, value):
        self.dll = LinkedList.insert(self, value)

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
