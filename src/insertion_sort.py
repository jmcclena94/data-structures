# coding=utf-8
import random


def insertion_sort(a_list):
    """Take a list and sort it using insertion_sort."""
    for item in a_list[1:]:
        current_val_index = a_list.index(item)
        left_index = current_val_index - 1
        while left_index >= 0 and a_list[left_index] > item:
            a_list[left_index + 1] = a_list[left_index]
            left_index = left_index - 1
        a_list[left_index + 1] = item
    return a_list


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
        """Call insertion_sort on ordered list."""
        insertion_sort(ordered_list)

    def get_unordered_list():
        """Call insertion_sort on unordered list."""
        insertion_sort(unordered_list)

    def get_reversed_list():
        """Call insertion_sort on reversed list."""
        insertion_sort(reversed_list)

    print('The Insertion Sort function sorts a list item in comparison to the'
          ' other items in the list before it.')

    print('Insertion Sort time on an ordered list of 10000: ', timeit.timeit(
          'get_ordered_list', setup='from __main__ import get_ordered_list'))

    print('Insertion Sort time on an unordered list of 10000: ', timeit.timeit(
          'get_unordered_list', setup='from __main__ import get_unordered_list'
          ))

    print('Insertion Sort time on an reversed list of 10000: ', timeit.timeit(
          'get_reversed_list',
          setup='from __main__ import get_reversed_list'))
