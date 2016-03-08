# coding=utf-8
from linked_list import LinkedList
# from linked_list import Node


class Stack(object):

    def __init__(self, value):
        self.head = None
        self.length = 0
        self.stack = LinkedList.insert(self, value)

    def push(self, value):
        self.stack = LinkedList.insert(self, value)

    def pop(self):
        pop_val = LinkedList.pop(self)
        return pop_val
