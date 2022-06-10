# Conventions

## Coding conventions

### Python scripts

See [SCILPY coding standards](https://scil-documentation.readthedocs.io/en/latest/coding/scilpy.html)


### Docstring

Google-style conventions

```python
# Reference: https://queirozf.com/entries/python-docstrings-reference-examples#google-style

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
```