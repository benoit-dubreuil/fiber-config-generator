import typing

Numeric = typing.Union[int, float]

T_Numeric = typing.TypeVar('T_Numeric', int, float)

Vec2 = typing.Tuple[T_Numeric, T_Numeric]
Vec2i = Vec2[int]
Vec2f = Vec2[float]

Vec3 = typing.Tuple[T_Numeric, T_Numeric, T_Numeric]
Vec3i = Vec3[int]
Vec3f = Vec3[float]
