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
    traversal = new_bst.in_order()
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
    traversal = new_bst.pre_order()
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
    traversal = new_bst.prost_order()
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
    traversal = new_bst.breadth_first()
    for item in traversal:
        results.append(item)
    assert results == [10, 8, 15, 7, 9, 13, 20]

