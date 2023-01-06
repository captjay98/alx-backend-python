#!/usr/bin/env python3
"""Using mypy to fix this"""
from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """returns a zoomed in array"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return (zoomed_in, )
