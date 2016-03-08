# coding=utf-8


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        new_node_value = Node(value)
        if self.head is None:
            self.head = new_node_value
            self.length += 1
        else:
            new_node_value.next_node = self.head
            new_node_value.next_node.prev = new_node_value
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
        x = self.head
        if x is not None:
            while x.next_node is not None:
                if (x.value == value):
                    return x
                x = x.next_node
            if (x.value == value):
                return x

    def remove(self, value):
        node_val = self.search(value)
        prev_node = node_val.prev
        prev_node.next_node = node_val.next_node
        self.length -= 1

    def display(self):
        tup = []
        x = self.head
        while x is not None:
            tup.append(x.value)
            x = x.next_node
        tup = tuple(tup)
        print(tup)
        return tup
