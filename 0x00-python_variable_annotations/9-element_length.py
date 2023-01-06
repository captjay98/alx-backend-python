#!/usr/bin/env python3
"""Annotates function with the right parameters"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
