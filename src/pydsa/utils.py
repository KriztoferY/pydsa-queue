"""
Utilities
---
This submodule contains utility functions that aid implementing abstract data
types and algorithms.
"""

import ctypes
from typing import Type, Literal

__all__ = ('py_obj_array_type', 'ElemTypeName', 'validate_close_range')


ElemTypeName = Literal['int', 'uint', 'float', 'double', 'object']


def py_obj_array_type(size: int, item_type: ElemTypeName = None) -> Type:
    """
    Creates and returns a type that represents contiguous memory cells for
    ``n`` objects of ``item_type``.

    Parameters
    ----------
    item_type : ElemTypeName
        Array item type -- 'int' | 'uint' | 'float' | 'double' | 'object'
    """
    if item_type is not None:
        if item_type == 'int':
            item_type = ctypes.c_longlong
        elif item_type == 'uint':
            item_type = ctypes.c_ulonglong
        elif item_type == 'float':
            item_type = ctypes.c_float
        elif item_type == 'double':
            item_type = ctypes.c_longdouble
        else:
            raise ValueError('Invalid argument item_type')
    else:
        item_type = ctypes.py_object
    return item_type * size


def is_pos_power_of_two(num: int) -> bool:
    """
    Returns ``True`` if ``n`` is a positive power of 2.
    """
    return num > 0 and (num & (num - 1) == 0)


def validate_close_range(name: str, value: int, low: int, high: int,
                         error: Type[Exception] = IndexError) -> None:
    """Raises ``error`` if ``value`` falls out of the close range ``[low, high].
    """
    if value < low or value > high:
        raise error(f'{name}={value} out of range [{low}, {high}]')
