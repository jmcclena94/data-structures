# coding=utf-8
# import random
import subprocess


class Node(object):
    """Create a binary search tree node."""

    def __init__(self, value):
        """Init."""
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def in_order(self):
        """Yield a list of ordered nodes left, parent, right."""
        if self.left:
            for item in self.left.in_order():
                yield item
        yield self.value
        if self.right:
            for item in self.right.in_order():
                yield item

    def pre_order(self):
        """Yield a list of ordered nodes parent, left, right."""
        yield self.value
        if self.left:
            for item in self.left.pre_order():
                yield item
        if self.right:
            for item in self.right.pre_order():
                yield item


class Bst(object):
    """Create a binary search tree."""

    def __init__(self):
        """Init."""
        self.size = 0
        self.head = None

    # def get_dot(self):
    #     """Return tree with root 'self' as a dot graph for visualization."""
    #     return "digraph G{\n%s}" % ("" if self.head is None else (
    #         "\t%s;\n%s\n" % (
    #             self.head,
    #             "\n".join(self._get_dot())
    #         )
    #     ))

    # def _get_dot(self):
    #     """Recursively prepare a dot graph entry for this node."""
    #     if self.left is not None:
    #         yield "\t%s -> %s;" % (self.head, self.left.value)
    #         for i in self.left._get_dot():
    #             yield i
    #     elif self.right is not None:
    #         r = random.randint(0, 1e9)
    #         yield "\tnull%s [shape=point];" % r
    #         yield "\t%s -> null%s;" % (self.head, r)
    #     if self.right is not None:
    #         yield "\t%s -> %s;" % (self.head, self.right.value)
    #         for i in self.right._get_dot():
    #             yield i
    #     elif self.left is not None:
    #         r = random.randint(0, 1e9)
    #         yield "\tnull%s [shape=point];" % r
    #         yield "\t%s -> null%s;" % (self.head, r)

    def insert(self, val):
        """Insert node into bst."""
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
        """Return true or false if the value exists or not."""
        current_node = self.head
        while current_node:
            if current_node.value == val:
                return True
            if current_node.value > val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def get_size(self):
        """Return the size of the tree."""
        return self.size

    def depth(self):
        """Return the depth of the tree."""
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

    def balance(self):
        """Return an integer indicating balance."""
        if self.head is None:
            return 0
        temp = self.head
        self.head = temp.left
        left_balance = self.depth()
        self.head = temp.right
        right_balance = self.depth()
        total_balance = left_balance - right_balance
        self.head = temp
        return total_balance

    def tree_traversal(self, traversal):
        """Call in_order generator and yield the items in the tree."""
        if traversal == 'in_order':
            if self.head:
                for item in self.head.in_order():
                    yield item
        if traversal == 'pre_order':
            if self.head:
                for item in self.head.pre_order():
                    yield item
        if traversal == 'post_order':
            if self.head:
                for item in self.head.post_order():
                    yield item
        if traversal == 'breadth':
            pass

    # def pre_order(self):
    #     """Call in_order generator and yield the items in the tree."""


# if __name__ == '__main__':
    # x = range(10)
    # bst = Bst()
    # for i in x:
    #     bst.insert(i)
    # dot_graph = bst.get_dot()
    # t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    # t.communicate(dot_graph)
