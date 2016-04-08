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

    # def _delete(self):
    #     """Delete instance of Node."""
    #     if self.right:
    #         if self.right is None and self.left is None:
    #             self.parent.right = None
    #         self.value = self.right.value
    #         self.right._delete()
    #         # if self.right is None and self.left is None:
    #         #     self.parent.right = None
    #     else:
    #         self.value = self.left.value
    #         self.left._delete()
    #         if self.right is None and self.left is None:
    #             self.parent.left = None


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
            yield self.head.value
            if self.head:
                for item in self.head.breadth_first():
                    yield item

    def delete(self, val):
        """Delete the node that has the value passed."""
        # import pdb; pdb.set_trace()
        if self.head:
            for item in self.head._search():
                if item.value == val:
                    if item.right:
                        temp_right = item.right
                        item.value = item.right.value
                        item.right.parent = None
                        item.right = None
                        for data in temp_right.in_order():
                            self.insert(data)
                    else:
                        if item.left:
                            temp_left = item.left
                            item.value = item.left.value
                            item.left.parent = None
                            item.left = None
                            for data in temp_left.in_order():
                                self.insert(data)
                        else:
                            if item.parent is None:
                                self.head = None
                            else:
                                if item.parent.right == item:
                                    item.parent.right = None
                                    item.parent = None
                                else:
                                    item.parent.left = None
                                    item.parent = None



                # if item.value == val and item == self.head:
                #     item._delete()
                #     self.head = None
                # elif item.value == val:
                #     item._delete()
