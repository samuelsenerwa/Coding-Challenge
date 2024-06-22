#!/usr/bin/python3

"""
A function that retrieves element from a list like C
"""


def element_at(my_list, idx):
    if idx < 0:
        return None
    length = len(my_list)
    if idx > length - 1:
        return None
    return my_list[idx]


# testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
