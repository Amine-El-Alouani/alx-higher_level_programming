#!/usr/bin/python3


def print_sorted_dictionary(a_dict):
    [print("{}: {}".format(k, a_dict[k])) for k in sorted(a_dict)]
