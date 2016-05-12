# coding=utf-8
def test_insertion_sort_on_small_list():
    """Test insertion_sort on a 5 item unordered."""
    from insertion_sort import insertion_sort
    test_list = [0, 5, 6, 2, 4]
    assert insertion_sort(test_list) == [0, 2, 4, 5, 6]


def test_insertion_sort_on_ordered_small_list():
    """Test insertion_sort on a 5 item ordered."""
    from insertion_sort import insertion_sort
    test_list = [0, 2, 4, 5, 6]
    assert insertion_sort(test_list) == [0, 2, 4, 5, 6]


def test_isertion_sort_on_reverse_ordered_small_list():
    """Test insertion_sort on a 5 item reverse oredered list."""
    from insertion_sort import insertion_sort
    test_list = [6, 5, 4, 2, 0]
    assert insertion_sort(test_list) == [0, 2, 4, 5, 6]


def test_with_floats():
    """Test insertion_sort functions on 5 item list with floats."""
    from insertion_sort import insertion_sort
    test_list = [0.6, 5.5, 6.2, 2.7, 4]
    assert insertion_sort(test_list) == [0.6, 2.7, 4, 5.5, 6.2]


def test_with_strings():
    """Test insertion_sort on list that has string values."""
    from insertion_sort import insertion_sort
    test_list = ['Joe', 'Mike', 'Jared']
    assert insertion_sort(test_list) == ['Jared', 'Joe', 'Mike']
