import typing

T_Numeric = typing.TypeVar('T_Numeric', int, float)

Vector3 = typing.Tuple[T_Numeric, T_Numeric, T_Numeric]
Vector3i = Vector3[int]
Vector3f = Vector3[float]
