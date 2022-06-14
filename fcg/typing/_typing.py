import typing

Numeric = typing.Union[int, float]

T_numeric = typing.TypeVar('T_numeric', int, float)

Vec2 = typing.Tuple[T_numeric, T_numeric]
Vec2i = Vec2[int]
Vec2f = Vec2[float]

Vec3 = typing.Tuple[T_numeric, T_numeric, T_numeric]
Vec3i = Vec3[int]
Vec3f = Vec3[float]
