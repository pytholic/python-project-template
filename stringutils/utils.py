"""Package utility functions.

Created by @pytholic on 2024.02.21
"""

from typing import List, TypeVar

import numpy as np

T = TypeVar("T", bound=List[str])


def reverse_string(input_str: str) -> str:
    """Function to reverse an input string."""
    return input_str[::-1]


def capitalize_string(input_str: str) -> str:
    """Function to capitalize all letters of an input string."""
    return input_str.upper()


def add_list_elements(input_list1: T, input_list2: T) -> T:
    """This functions take two string lists and performs element-wise concatenation. Lists must
    have the same shape.

    Parameters
    ----------
    input_list1 : List[str]
        A list of strings
    input_list2 : List[str]
        A list of strings

    Returns
    -------
    List[str]
        Output list of strings.

    Notes
    -----
    This function originally works with both lists and arrays. However, output is
    ndarray. To keep things consistent, I converted output array to a list.

    Reference
    -----
    .. [1] https://numpy.org/doc/stable/reference/generated/numpy.char.add.html#numpy.char.add
    """
    return list(np.char.add(input_list1, input_list2))
