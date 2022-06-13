import typing
import dataclasses


@dataclasses.dataclass(frozen=True)
class World:
    resolution: typing.Tuple[int, int, int]
