"""
This module `pydsa.utils` contains utility functions that aid implementing 
abstract data types and algorithms.
"""

import ctypes
from typing import Type, Literal

__all__ = ('py_obj_array_type', 'ElemTypeName', 'validate_close_range')


ElemTypeName = Literal['int', 'uint', 'float', 'double', 'object']
"""All possible options for contiguous memory cell item type.
"""


def py_obj_array_type(size: int, item_type: ElemTypeName) -> Type:
    """Creates and returns a type that represents contiguous memory cells for
    `size` number of objects of `item_type`.

    Args:
        item_type (ElemTypeName): Cell item type -- 'int', 'uint', 'float', 
        'double', 'object'.

    Raises:
        ValueError: if `item_type` is not one of allowed options.

    Returns:
        Type: The contiguous memory cell type desired.

    See Also:
        `pydsa.utils.ElemTypeName`
    """
    if item_type == 'int':
        item_type = ctypes.c_longlong
    elif item_type == 'uint':
        item_type = ctypes.c_ulonglong
    elif item_type == 'float':
        item_type = ctypes.c_float
    elif item_type == 'double':
        item_type = ctypes.c_longdouble
    elif item_type == 'object':
        item_type = ctypes.py_object
    else:
        raise ValueError('Invalid argument item_type')
    return item_type * size


def is_pos_power_of_two(num: int) -> bool:
    """Checks if `num` is a positive power of 2.

    Args:
        num (int): The number to test.

    Returns:
        bool: `True` if `num` is a positive power of 2, `False` otherwise.
    """
    return num > 0 and (num & (num - 1) == 0)


def validate_close_range(name: str, value: int, low: int, high: int,
                         error: Type[Exception] = IndexError) -> None:
    """Checks if the number `value` falls within the close range `[low, 
    high]`.

    Args:
        name (str): Name of the number to check.
        value (int): The number to check. 
        low (int): Beginning of the close range.
        high (int): End of the close range.
        error (Type[Exception], optional): The exception type to raise when the test fails. 

    Raises:
        error: if `value` falls outside the close range `[low, high]`.
    """
    if value < low or value > high:
        raise error(f'{name}={value} out of range [{low}, {high}]')
