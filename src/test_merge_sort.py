# coding=utf-8


def test_merge_sort():
    """Test merge sort on random list."""
    from merge_sort import merge_sort
    test_list = [0, 5, 6, 2, 4]
    assert merge_sort(test_list) == [0, 2, 4, 5, 6]


def test_merge_sort_string():
    """Test merge sort on a string."""
    from merge_sort import merge_sort
    test_list = ['Joe', 'Jared', 'Mike']
    assert merge_sort(test_list) == ['Jared', 'Joe', 'Mike']
