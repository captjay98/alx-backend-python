#!/usr/bin/env python3
"""
a type-annotated function to_kv that takes
a string k and an int OR float v as arguments
and returns a tuple.
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns square of v as float"""
    return k, v**2
