# coding=utf-8


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

    def post_order(self):
        """Yield a list of ordered nodes left, right, parent."""
        if self.left:
            for item in self.left.post_order():
                yield item
        if self.right:
            for item in self.right.post_order():
                yield item
        yield self.value

    def breadth_first(self):
        """Yield a list of ordered nodes."""
        if self.left:
            yield self.left.value
        if self.right:
            yield self.right.value
        if self.left:
            for item in self.left.breadth_first():
                yield item
        if self.right:
            for item in self.right.breadth_first():
                yield item

    def _search(self):
        """Yield a list of ordered nodes left, parent, right."""
        if self.left:
            for item in self.left._search():
                yield item
        yield self
        if self.right:
            for item in self.right._search():
                yield item

    def left_right_conversion(self):
        """Convert left-right case to a left-left case."""
        self.left = self.left.right
        temp = self.left.left
        self.left.left = self.left.parent
        self.left.parent = self
        self.left.left.parent = self.left
        self.left.left.right = temp

    def right_left_conversion(self):
        """Convert right-left case to a right-right case."""
        self.right = self.right.left
        temp = self.right.right
        self.right.right = self.right.parent
        self.right.parent = self
        self.right.right.parent = self.right
        self.right.right.left = temp

    def left_rotation(self):
        """Rotate three node structure counter clockwise."""
        self.right.parent = self.parent
        try:
            self.parent.right = self.right
        except AttributeError:
            pass
        self.parent = self.right
        temp = self.right.left
        self.right.left = self
        self.right = temp

    def right_rotation(self):
        """Rotate three node structure clockwise."""
        self.left.parent = self.parent
        try:
            self.parent.left = self.left
        except AttributeError:
            pass
        self.parent = self.left
        temp = self.left.right
        self.left.right = self
        self.left = temp

    def depth(self):
        """Find the depth of the tree from the node."""
        to_visit = [self]
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

    def check_balance(self):
        """Check balance of the tree based on the inserted Node."""
        try:
            right_depth = self.right.depth()
        except:
            right_depth = 0
        try:
            left_depth = self.left.depth()
        except:
            left_depth = 0
        balance = left_depth - right_depth
        return balance


class Bst(object):
    """Create a binary search tree."""

    def __init__(self):
        """Init."""
        self.size = 0
        self.head = None

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
                    flag = False
        if new_node.parent:
            self.self_balance(new_node)

    def self_balance(self, node):
        """Auto balance the tree after insertion."""
        parent_node = node.parent
        current_node = node
        while parent_node:
            parent_balance = parent_node.check_balance()
            if parent_balance > 1:
                if parent_node.left.check_balance() < 0:
                    parent_node.left_right_conversion()
                    parent_node.right_rotation()
                else:
                    parent_node.right_rotation()
            elif parent_balance < -1:
                if parent_node.right.check_balance() > 0:
                    parent_node.right_left_conversion()
                    parent_node.left_rotation()
                else:
                    parent_node.left_rotation()
            current_node = parent_node
            parent_node = parent_node.parent
        self.head = current_node

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
            yield self.head.value
            if self.head:
                for item in self.head.breadth_first():
                    yield item

    def _deal_with_child(self, item):
        """Insert and delete child nodes."""
        temp = item
        item.parent.value = item.value
        if item.parent.right == item:
            item.parent.right = None
        else:
            item.parent.left = None
        item.parent = None
        item = None
        for data in temp.pre_order():
            self.insert(data)
            self.size -= 1

    def _leaf_check_and_delete(self, item):
        """Severe parent child connection for leaf."""
        if item.parent.right == item:
            item.parent.right = None
            item.parent = None
        else:
            item.parent.left = None
            item.parent = None

    def delete(self, val):
        """Delete the node that has the value passed."""
        if self.head:
            self.size -= 1
            for item in self.head._search():
                if item.value == val:
                    if item.right:
                        self._deal_with_child(item.right)
                    else:
                        if item.left:
                            self._deal_with_child(item.left)
                        else:
                            if item.parent is None:
                                self.head = None
                            else:
                                self._leaf_check_and_delete(item)
