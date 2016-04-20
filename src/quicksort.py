# coding=utf-8
import random


def quick_sort(a_list, lo, hi):
    """Quicksort."""
    if lo < hi:
        part, a_list = partition(a_list, lo, hi)
        quick_sort(a_list, lo, part - 1)
        quick_sort(a_list, part + 1, hi)
    return a_list


def partition(a_list, lo, hi):
    """Partition."""
    pivot = a_list[hi]
    idx = lo
    for index in range(lo, hi):
        if a_list[index] <= pivot:
            temp = a_list[idx]
            a_list[idx] = a_list[index]
            a_list[index] = temp
            idx += 1
    temp = a_list[idx]
    a_list[idx] = a_list[hi]
    a_list[hi] = temp
    pivot_point = idx
    return pivot_point, a_list


# if __name__ == '__main__':
#     """Run in console."""
#     import timeit

#     ordered_list = []
#     unordered_list = []
#     reversed_list = []

#     for item in range(10000):
#         ordered_list.append(item)

#     for item in range(10000):
#         unordered_list.append(random.randint(0, 10000))

#     for item in range(10000, 0, -1):
#         reversed_list.append(item)

#     def get_ordered_list():
#         """Call merge_sort on ordered list."""
#         merge_sort(ordered_list)

#     def get_unordered_list():
#         """Call merge_sort on unordered list."""
#         merge_sort(unordered_list)

#     def get_reversed_list():
#         """Call merge_sort on reversed list."""
#         merge_sort(reversed_list)

#     print('The Merge Sort function sorts a list item in comparison to the'
#           ' other items in the list before it.')

#     print('Merge Sort time on an ordered list of 10000: ', timeit.timeit(
#           'get_ordered_list', setup='from __main__ import get_ordered_list'))

#     print('Merge Sort time on an unordered list of 10000: ', timeit.timeit(
#           'get_unordered_list', setup='from __main__ import get_unordered_list'
#           ))

#     print('Merge Sort time on an reversed list of 10000: ', timeit.timeit(
#           'get_reversed_list',
#           setup='from __main__ import get_reversed_list'))
