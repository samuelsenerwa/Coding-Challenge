#!/usr/bin/python3
"""
Write a function that replaces an element of a list at a specific position 
"""


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    length = len(my_list)
    if idx > length - 1:
        return None
    return my_list[idx]
