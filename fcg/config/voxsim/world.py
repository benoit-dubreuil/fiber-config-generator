import typing
import dataclasses


@dataclasses.dataclass(frozen=True)
class World:
    resolution: (int, int, int)
