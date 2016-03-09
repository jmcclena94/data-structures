# coding=utf-8


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):

    def __init__(self):
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
        pop_value = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return pop_value

    def size(self):
        return self.length

    def search(self, value):
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                if (current_node.value == value):
                    return current_node
                current_node = current_node.next_node
            if (current_node.value == value):
                return current_node

    def remove(self, value):
        current_node = self.head
        if current_node is not None:
            while current_node.next_node is not None:
                if (current_node.next_node.value == value):
                    current_node.next_node = current_node.next_node.next_node
                    self.length -= 1
                current_node = current_node.next_node

    def display(self):
        tup = []
        x = self.head
        while x is not None:
            tup.append(x.value)
            x = x.next_node
        tup = tuple(tup)
        print(tup)
        return tup
