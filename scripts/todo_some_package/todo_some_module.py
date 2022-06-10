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


# TODO: Disable mandatory docstring for private functions
def _some_func() -> str:
    return 'test'

    # Example of Google-style docstring

    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `arg2` is equal to `arg1`.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> a=1
        >>> b=2
        >>> func(a,b)
        True

    """
