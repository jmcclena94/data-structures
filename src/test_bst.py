# coding=utf-8


def test_node_class():
    """Init node."""
    from bst import Node
    node = Node(5)
    assert node.value == 5
    assert node.right is None
    assert node.left is None
    assert node.parent is None


def test_insert():
    """Test if value inserted into the tree."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    assert new_bst.head.value == 3


def test_insert_two_values():
    """Test insert works for two values."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(4)
    assert new_bst.head.value == 3
    assert new_bst.head.right.value == 4
    assert new_bst.head.left is None


def test_insert_three_values():
    """Test three values."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(5)
    new_bst.insert(4)
    assert new_bst.head.value == 3
    assert new_bst.head.right.value == 5
    assert new_bst.head.right.left.value == 4


def test_insert_value_already_exists():
    """Test if value exists it is ignored."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(3)
    assert new_bst.head.right is None
    assert new_bst.head.left is None
    assert new_bst.head.value == 3


def test_contain_true():
    """Test if value in list return True."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    assert new_bst.contains(3) is True


def test_contain_false():
    """Test if value in list return False."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    assert new_bst.contains(4) is False


def test_get_size():
    """Test the size method works."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(8)
    new_bst.insert(5)
    assert new_bst.get_size() == 3


def test_depth():
    """Test depth works."""
    from bst import Bst
    r = range(10)
    new_bst = Bst()
    for i in r:
        new_bst.insert(i)
    assert new_bst.depth() == 10


def test_balance_left_two_nodes():
    """Test balance left heavy."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(2)
    assert new_bst.balance() == 1


def test_balance_right_two_nodes():
    """Test balance right heavy."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(4)
    assert new_bst.balance() == -1


def test_balance_equal():
    """Test that tree is balanced."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(3)
    new_bst.insert(2)
    new_bst.insert(4)
    assert new_bst.balance() == 0


def test_balance_empty_list():
    """Test returns 0 if tree is empty."""
    from bst import Bst
    new_bst = Bst()
    assert new_bst.balance() == 0


def test_balance_right_complex():
    """Test a right heavy list with multiple nodes."""
    from bst import Bst
    r = range(10)
    new_bst = Bst()
    for i in r:
        new_bst.insert(i)
    assert new_bst.balance() == -9


def test_balance_left_complex():
    """Test a left heavy list with multiple nodes."""
    from bst import Bst
    r = range(10, 0, -1)
    new_bst = Bst()
    for i in r:
        new_bst.insert(i)
    assert new_bst.balance() == 9


def test_balance_equal_complex():
    """Test a balanced list with multiple nodes."""
    from bst import Bst
    r1 = range(5, 0, -1)
    new_bst = Bst()
    for i in r1:
        new_bst.insert(i)
    r2 = range(10, 14)
    for i in r2:
        new_bst.insert(i)
    assert new_bst.balance() == 0


def test_in_order():
    """Test if function returns nodes in order of left, parent, right."""
    from bst import Bst
    tree_vals = [10, 8, 15, 7, 9, 13, 20]
    results = []
    new_bst = Bst()
    for val in tree_vals:
        new_bst.insert(val)
    traversal = new_bst.tree_traversal('in_order')
    for item in traversal:
        results.append(item)
    assert results == [7, 8, 9, 10, 13, 15, 20]


def test_pre_order():
    """Test if function returns nodes in order of parent, left, right."""
    from bst import Bst
    tree_vals = [10, 8, 15, 7, 9, 13, 20]
    results = []
    new_bst = Bst()
    for val in tree_vals:
        new_bst.insert(val)
    traversal = new_bst.tree_traversal('pre_order')
    for item in traversal:
        results.append(item)
    assert results == [10, 8, 7, 9, 15, 13, 20]


def test_post_order():
    """Test if function returns nodes in order of parent, left, right."""
    from bst import Bst
    tree_vals = [10, 8, 15, 7, 9, 13, 20]
    results = []
    new_bst = Bst()
    for val in tree_vals:
        new_bst.insert(val)
    traversal = new_bst.tree_traversal('post_order')
    for item in traversal:
        results.append(item)
    assert results == [7, 9, 8, 13, 20, 15, 10]


def test_breadth_first():
    """Test if function returns nodes in order of parent, left, right."""
    from bst import Bst
    tree_vals = [10, 8, 15, 7, 9, 13, 20]
    results = []
    new_bst = Bst()
    for val in tree_vals:
        new_bst.insert(val)
    traversal = new_bst.tree_traversal('breadth')
    for item in traversal:
        results.append(item)
    assert results == [10, 8, 15, 7, 9, 13, 20]


def test_delete():
    """Test that the selected node is deleted."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(1)
    new_bst.delete(1)
    assert new_bst.contains(1) is False
    assert new_bst.head is None
    assert new_bst.size == 0


def test_delete_on_range():
    """Test that the node selected is removed from the tree."""
    from bst import Bst
    new_bst = Bst()
    for items in range(20):
        new_bst.insert(items)
    new_bst.delete(10)
    assert new_bst.contains(10) is False
    assert new_bst.size == 19


def test_delete_on_small_range():
    """Test that the node selected is removed from the tree."""
    from bst import Bst
    new_bst = Bst()
    for items in range(5):
        new_bst.insert(items)
    new_bst.delete(1)
    assert new_bst.contains(1) is False
    assert new_bst.size == 4
    assert new_bst.head.right.value == 2
    assert new_bst.head.right.right.value == 3
    assert new_bst.head.right.right.right.value == 4
    assert new_bst.head.right.right.right.right is None
    assert new_bst.head.left is None


def test_edge_cases_delete_tree():
    """Test deletion on tree from EdgeCases example tree."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(20)
    new_bst.insert(5)
    new_bst.delete(10)
    assert new_bst.contains(10) is False
    assert new_bst.size == 2
    assert new_bst.head.value == 20
    assert new_bst.head.right is None
    assert new_bst.head.left.value == 5


def test_off_balance_delete_tree():
    """Test deletion on tree from complex tree."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(20)
    new_bst.insert(5)
    new_bst.insert(15)
    new_bst.insert(25)
    new_bst.delete(10)
    assert new_bst.contains(10) is False
    assert new_bst.size == 4
    assert new_bst.head.value == 20
    assert new_bst.head.right.value == 25
    assert new_bst.head.left.value == 5
    assert new_bst.head.left.right.value == 15


def test_off_balance_delete_tree_non_head():
    """Test deletion on tree from complex tree."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(20)
    new_bst.insert(5)
    new_bst.insert(15)
    new_bst.insert(25)
    new_bst.delete(20)
    assert new_bst.contains(20) is False
    assert new_bst.size == 4
    assert new_bst.head.value == 10
    assert new_bst.head.right.value == 25
    assert new_bst.head.left.value == 5
    assert new_bst.head.right.left.value == 15


def test_delete_on_complex_tree():
    """Test that the selected node is deleted."""
    from bst import Bst
    nodes = [10, 9, 15, 2, 6, 12, 20, 1, 3]
    new_bst = Bst()
    for item in nodes:
        new_bst.insert(item)
    new_bst.delete(2)
    assert new_bst.contains(2) is False


def test_search():
    """Test that the search returns a node connected to the selected value."""
    from bst import Bst, Node
    new_bst = Bst()
    new_bst.insert(1)
    for item in new_bst.head._search():
        assert isinstance(item, Node)


def test_left_right_conversion_three_nodes():
    """Test that given three nodes in a left-right state converts to left-left."""
    from bst import Bst, Node
    new_bst = Bst()
    node1 = Node(15)
    node2 = Node(10)
    node3 = Node(12)
    new_bst.head = node1
    node1.left = node2
    node2.parent = node1
    node2.right = node3
    node3.parent = node2
    new_bst.head.left_right_conversion()
    assert new_bst.head.left == node3
    assert new_bst.head.left.left == node2
    assert new_bst.head.left.left.parent == node3
    assert new_bst.head.left.parent == node1


def test_left_right_conversion_six_nodes():
    """Test that given six nodes in a left-right state converts to left-left."""
    from bst import Bst, Node
    new_bst = Bst()
    node1 = Node(10)
    node2 = Node(15)
    node3 = Node(5)
    node4 = Node(3)
    node5 = Node(8)
    node6 = Node(9)
    new_bst.head = node1
    node1.left = node3
    node3.parent = node1
    node3.left = node4
    node4.parent = node3
    node3.right = node5
    node5.parent = node3
    node5.right = node6
    node6.parent = node5
    node1.right = node2
    node2.parent = node1
    new_bst.head.left_right_conversion()
    assert new_bst.head.left == node5
    assert new_bst.head.left.right == node6
    assert new_bst.head.left.left == node3


def test_right_left_conversion_three_nodes():
    """Test that given three nodes in a right-left state converts to right-right."""
    from bst import Bst, Node
    new_bst = Bst()
    node1 = Node(10)
    node2 = Node(15)
    node3 = Node(12)
    new_bst.head = node1
    node1.right = node2
    node2.parent = node1
    node2.left = node3
    node3.parent = node2
    new_bst.head.right_left_conversion()
    assert new_bst.head.right == node3
    assert new_bst.head.right.right == node2
    assert new_bst.head.right.right.parent == node3
    assert new_bst.head.right.parent == node1


def test_right_left_conversion_six_nodes():
    """Test that given six nodes in a left-right state converts to left-left."""
    from bst import Bst, Node
    new_bst = Bst()
    node1 = Node(10)
    node2 = Node(5)
    node3 = Node(15)
    node4 = Node(20)
    node5 = Node(14)
    node6 = Node(13)
    new_bst.head = node1
    node1.left = node2
    node2.parent = node1
    node1.right = node3
    node3.parent = node1
    node3.right = node4
    node4.parent = node3
    node3.left = node5
    node5.parent = node3
    node5.left = node6
    node6.parent = node5
    new_bst.head.right_left_conversion()
    assert new_bst.head.right == node5
    assert new_bst.head.right.right == node3
    assert new_bst.head.right.right.right == node4


def test_right_rotation_three_nodes():
    """Test that a left-left becomes balanced."""
    from bst import Bst, Node
    new_bst = Bst()
    node1 = Node(15)
    node2 = Node(10)
    node3 = Node(5)
    new_bst.head = node1
    node1.left = node2
    node2.parent = node1
    node2.left = node3
    node3.parent = node2
    new_bst.head.right_rotation()
    assert node2.parent is None
    assert node2.right == node1
    assert node2.left == node3
    assert node2.right.parent == node2


def test_left_rotation_three_nodes():
    """Test that a right-right becomes balanced."""
    from bst import Bst, Node
    new_bst = Bst()
    node1 = Node(10)
    node2 = Node(15)
    node3 = Node(20)
    new_bst.head = node1
    node1.right = node2
    node2.parent = node1
    node2.right = node3
    node3.parent = node2
    new_bst.head.left_rotation()
    assert node2.parent is None
    assert node2.left == node1
    assert node2.right == node3
    assert node2.left.parent == node2


def test_depth_from_node_three_nodes():
    """Test the depth of the tree from a node."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(15)
    new_bst.insert(20)
    # fails until balancing function is created
    assert new_bst.head.depth() == 3
    assert new_bst.head.right.depth() == 2


def test_check_balance_right_right():
    """Test for balance of tree from selected Node."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(10)
    new_bst.insert(15)
    new_bst.insert(20)
    assert new_bst.balance() == -2


def test_check_balance_left_left():
    """Test for balance of tree from selected Node."""
    from bst import Bst
    new_bst = Bst()
    new_bst.insert(15)
    new_bst.insert(12)
    new_bst.insert(10)
    assert new_bst.balance() == 2
