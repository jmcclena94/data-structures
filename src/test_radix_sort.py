# coding=utf-8


def test_radix_sort():
    """Test Radix sort."""
    from radix_sort import radix_sort
    unsorted_list = [5, 28, 90, 6, 42, 39]
    assert radix_sort(unsorted_list) == [5, 6, 28, 39, 42, 90]


def test_radix_sort_on_empty():
    """Test Radix sort on an empty list."""
    from radix_sort import radix_sort
    empty_list = []
    assert radix_sort(empty_list) == []


def test_radix_sort_on_one():
    """Test Radix sort on 1 item list."""
    from radix_sort import radix_sort
    one_list = [1]
    assert radix_sort(one_list) == [1]
