# coding=utf-8


class Node(object):
    """Create a binary search tree node."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Bst(object):
    """Create a binary search tree."""

    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        self.size += 1
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            flag = True
            while flag:
                if (current_node.left is not None) & (
                        current_node.value > val):
                    current_node = current_node.left
                elif (current_node.right is not None) & (
                        current_node.value < val):
                    current_node = current_node.right
                elif current_node.value > val:
                    current_node.left = new_node
                    new_node.parent = current_node
                    flag = False
                elif current_node.value < val:
                    current_node.right = new_node
                    new_node.parent = current_node
                    flag = False
                else:
                    break

    def contains(self, val):
        current_node = self.head
        while current_node:
            if current_node.value == val:
                return True
            if current_node.value > val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def size(self):
        return self.size

    def depth(self):
        if self.head is None:
            return 0
        to_visit = [self.head]
        depths_visited = [1]
        tree_depth = 0
        while to_visit:
            current_node = to_visit.pop()
            current_dep = depths_visited.pop()
            if tree_depth < current_dep:
                tree_depth = current_dep
            if current_node.left is not None:
                to_visit.append(current_node.left)
                depths_visited.append(current_dep + 1)
            if current_node.right is not None:
                to_visit.append(current_node.right)
                depths_visited.append(current_dep + 1)
        return tree_depth
