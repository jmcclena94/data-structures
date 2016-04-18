# coding=utf-8


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


# if __name__ == '__main__':
