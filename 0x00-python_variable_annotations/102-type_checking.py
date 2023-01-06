#!/usr/bin/env python3
"""Using mypy to fix this"""


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """returns a zoomed in array"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
