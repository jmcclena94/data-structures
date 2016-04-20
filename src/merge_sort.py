# coding=utf-8
import random


def merge_sort(lst):
    """Sort an unsorted list using merge sort."""
    mpt = len(lst) >> 1
    lst_a = lst[:mpt]
    lst_b = lst[mpt:]

    if len(lst_a) > 1:
        sublist_a = merge_sort(lst_a)
    else:
        sublist_a = lst_a
    if len(lst_b) > 1:
        sublist_b = merge_sort(lst_b)
    else:
        sublist_b = lst_b

    idx_a = 0
    idx_b = 0
    flag = True
    merge_sublist = []
    while flag:
        try:
            if sublist_a[idx_a] < sublist_b[idx_b]:
                merge_sublist.append(sublist_a[idx_a])
                idx_a += 1
            else:
                merge_sublist.append(sublist_b[idx_b])
                idx_b += 1
        except IndexError:
            if idx_a >= len(sublist_a):
                merge_sublist = merge_sublist + sublist_b[idx_b:]
            else:
                merge_sublist = merge_sublist + sublist_a[idx_a:]
            flag = False
    return merge_sublist


if __name__ == '__main__':
    """Run in console."""
    import timeit

    ordered_list = []
    unordered_list = []
    reversed_list = []

    for item in range(10000):
        ordered_list.append(item)

    for item in range(10000):
        unordered_list.append(random.randint(0, 10000))

    for item in range(10000, 0, -1):
        reversed_list.append(item)

    def get_ordered_list():
        """Call merge_sort on ordered list."""
        merge_sort(ordered_list)

    def get_unordered_list():
        """Call merge_sort on unordered list."""
        merge_sort(unordered_list)

    def get_reversed_list():
        """Call merge_sort on reversed list."""
        merge_sort(reversed_list)

    print('The Merge Sort function sorts a list item in comparison to the'
          ' other items in the list before it.')

    print('Merge Sort time on an ordered list of 10000: ', timeit.timeit(
          'get_ordered_list', setup='from __main__ import get_ordered_list'))

    print('Merge Sort time on an unordered list of 10000: ', timeit.timeit(
          'get_unordered_list', setup='from __main__ import get_unordered_list'
          ))

    print('Merge Sort time on an reversed list of 10000: ', timeit.timeit(
          'get_reversed_list',
          setup='from __main__ import get_reversed_list'))
