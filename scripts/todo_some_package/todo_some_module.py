# -*- coding: utf-8 -*-

"""
TODO
"""

import typing

__all__: typing.Sequence[str] = ['print_some_func_ret']


def print_some_func_ret(arg1: int) -> None:
    """Prints the return value of the function _some_func.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
    """

    print(arg1)
    print(_some_func())


def _some_func() -> str:
    return 'test'
