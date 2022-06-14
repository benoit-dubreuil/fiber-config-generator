import typing

Numeric = typing.TypeVar('Numeric', int, float)

Vector3 = typing.Tuple[Numeric, Numeric, Numeric]
Vector3i = typing.Tuple[int, int, int]
Vector3f = typing.Tuple[float, float, float]
