#!/usr/bin/env python3
"""
 a type-annotated function that takes a float
 as argument and returns a function that multiplies a float
"""
from typing import callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """Returns a multiplier"""

    def multiplier_function(number:
                            float) -> float:
        """multiplies a number"""
        return multiplier * number

    return multiplier_function
