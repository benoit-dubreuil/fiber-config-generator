import typing

Numeric = typing.Union[int, float]

TNumeric = typing.TypeVar("TNumeric", int, float)

Vec2 = typing.Tuple[TNumeric, TNumeric]
Vec2i = Vec2[int]
Vec2f = Vec2[float]

Vec3 = typing.Tuple[TNumeric, TNumeric, TNumeric]
Vec3i = Vec3[int]
Vec3f = Vec3[float]
