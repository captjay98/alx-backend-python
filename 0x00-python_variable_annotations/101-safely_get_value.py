#!/usr/bin/env python3
"""Type annotation for function"""


def safely_get_value(dct, key, default = None):
    """Safely gets a value"""
    if key in dct:
        return dct[key]
    else:
        return default
