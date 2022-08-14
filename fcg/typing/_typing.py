import typing

Numeric: typing.TypeAlias = typing.Union[int, float]

TNumeric: typing.TypeAlias = typing.TypeVar("TNumeric", int, float)

Vec2: typing.TypeAlias = tuple[TNumeric, TNumeric]
Vec2i: typing.TypeAlias = Vec2[int]
Vec2f: typing.TypeAlias = Vec2[float]

Vec3: typing.TypeAlias = tuple[TNumeric, TNumeric, TNumeric]
Vec3i: typing.TypeAlias = Vec3[int]
Vec3f: typing.TypeAlias = Vec3[float]
