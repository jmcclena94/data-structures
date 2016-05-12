# coding=utf-8


def test_quick_sort():
    """Test quick sort on random list."""
    from quicksort import quick_sort
    test_list = [0, 5, 6, 2, 4]
    lo = 0
    hi = len(test_list) - 1
    assert quick_sort(test_list, lo, hi) == [0, 2, 4, 5, 6]


def test_quick_sort_string():
    """Test quick sort on a string."""
    from quicksort import quick_sort
    test_list = ['Joe', 'Jared', 'Mike']
    lo = 0
    hi = len(test_list) - 1
    assert quick_sort(test_list, lo, hi) == ['Jared', 'Joe', 'Mike']


def test_partition():
    """Test the partition returns a modified list and value we expect."""
    from quicksort import partition
    test_list = [0, 1]
    lo = 0
    hi = len(test_list) - 1
    pivot_point, a_list = partition(test_list, lo, hi)
    assert pivot_point == 1
    assert a_list == [0, 1]
