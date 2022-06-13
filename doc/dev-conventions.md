# Development conventions

## Coding conventions

See [`setup.cfg`](../setup.cfg) for technical details.


### Project folder structure

- `/scripts` — executable scripts from the CLI
- `/tests`
- `/fcg` — _Fiber Config Generator_ source files
- `/doc` — non-generated documation
- `/apidoc` — generated documation


### Python scripts

See [SCILPY coding standards](https://scil-documentation.readthedocs.io/en/latest/coding/scilpy.html) but keep in mind that since [PEP 3120](https://peps.python.org/pep-3120/),
UTF-8 is the default encoding for Python source code.

Avoid `__all__` because the `_` prefix defines what is public and what is not.
See [this post](https://stackoverflow.com/questions/44834/what-does-all-mean-in-python/35710527#35710527) for an explanation.

The line length is `120`, just as [LiNumPy](https://github.com/linum-uqam/linumpy).


### Docstring

NumPy style conventions

See comprehensive examples : https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html


```python
# Reference: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

def module_level_function(param1, param2=None, *args, **kwargs):
    r"""This is an example of a module level function.

    Function parameters should be documented in the ``Parameters`` section.
    The name of each parameter is required. The type and description of each
    parameter is optional, but should be included if not obvious.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name : type
            description

            The description may span multiple lines. Following lines
            should be indented to match the first line of the description.
            The ": type" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : :obj:`str`, optional
        The second parameter.
    *args
        Variable length argument list.
    **kwargs
        Arbitrary keyword arguments.

    Returns
    -------
    bool
        True if successful, False otherwise.

        The return type is not optional. The ``Returns`` section may span
        multiple lines and paragraphs. Following lines should be indented to
        match the first line of the description.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises
    ------
    AttributeError
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError
        If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True
```