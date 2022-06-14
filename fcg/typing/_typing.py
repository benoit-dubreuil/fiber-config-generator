import typing

Numeric = typing.TypeVar('Numeric', int, float)

Vector3 = typing.Tuple[Numeric, Numeric, Numeric]
Vector3i = Vector3[int]
Vector3f = Vector3[float]
