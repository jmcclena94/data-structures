# coding=utf-8
import random


def radix_sort(lst):
    """Sort by using Radix LSD alogrithm."""
    try:
        max_val = max(lst)
    except ValueError:
        return []
    tens_count = 1
    while tens_count < max_val:
        bucket_list = [0] * 10
        for num in lst:
            bucket_list[num // tens_count % 10] += 1
        for idx in range(1, len(bucket_list)):
            bucket_list[idx] += bucket_list[idx - 1]
        temp_list = [0] * len(lst)
        for num in reversed(lst):
            temp_list[bucket_list[num // tens_count % 10] - 1] = num
            bucket_list[num // tens_count % 10] -= 1
        lst = temp_list
        tens_count *= 10
    return lst

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
        """Call radix_sort on ordered list."""
        radix_sort(ordered_list)

    def get_unordered_list():
        """Call radix_sort on unordered list."""
        radix_sort(unordered_list)

    def get_reversed_list():
        """Call radix_sort on reversed list."""
        radix_sort(reversed_list)

    print('The Radix Sort function sorts a list item in comparison to the'
          ' other items in the list before it.')

    print('Radix Sort time on an ordered list of 10000: ', timeit.timeit(
          'get_ordered_list', setup='from __main__ import get_ordered_list'))

    print('Radix Sort time on an unordered list of 10000: ', timeit.timeit(
          'get_unordered_list', setup='from __main__ import get_unordered_list'
          ))

    print('Radix Sort time on an reversed list of 10000: ', timeit.timeit(
          'get_reversed_list',
          setup='from __main__ import get_reversed_list'))
