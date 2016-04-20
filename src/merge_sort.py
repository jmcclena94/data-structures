# coding=utf-8


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
