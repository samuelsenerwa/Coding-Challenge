#!/usr/bin/python3

"""
A function that prints all integers of a list, in reverse order

@function: Prototype: def print_reversed_list_integer(my_list=[]):

"""


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))


# Testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
