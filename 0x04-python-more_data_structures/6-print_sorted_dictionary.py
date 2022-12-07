#!/usr/bin/python3


def print_sorted_dictionary(a_dict):
    [print("{}: {}".format(f, a_dict[k])) for f in sorted(a_dict)]
