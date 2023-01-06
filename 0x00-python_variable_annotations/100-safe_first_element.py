#usr/bin/env python3
"""duck-typed annotations"""


def safe_first_element(lst):
    """returns first safe element"""
    if lst:
        return lst[0]
    else:
        return None
