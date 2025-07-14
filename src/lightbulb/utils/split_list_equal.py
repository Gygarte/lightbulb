def split_list_equal(
    lst: list[object],
) -> tuple[list[object], list[object], list[object]]:
    """Split a list into three approximately equal lists.

    Parameters
    ----------
    lst : list[object]
        The list to be split. Can contain any type of objects.

    Returns
    -------
    tuple[list[object], list[object], list[object]]
        A tuple containing three lists, each containing approximately one-third of the original list's elements.
        Empty lists will be returned if the number of elements in the input list is less than 3.
    """

    n = len(lst)
    chunk_size = n // 3
    remainder = n % 3

    first_end = chunk_size + (1 if remainder > 0 else 0)
    second_end = first_end + chunk_size + (1 if remainder > 1 else 0)

    list1 = lst[:first_end]
    list2 = lst[first_end:second_end]
    list3 = lst[second_end:]

    return list1, list2, list3
