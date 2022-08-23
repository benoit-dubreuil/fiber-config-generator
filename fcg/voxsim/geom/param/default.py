import typing

import fcg.typing

from .. import const as _geom_const

BUNDLE_N_FIBERS: typing.Final[int] = 800
BUNDLE_LIMITS: typing.Final[list[list[float]]] = [[0, 1], [0, 1], [0, 1]]
BUNDLE_CENTER: typing.Final[fcg.typing.Vec3f] = (
    (BUNDLE_LIMITS[0][0] + BUNDLE_LIMITS[0][1]) / 2,
    (BUNDLE_LIMITS[1][0] + BUNDLE_LIMITS[1][1]) / 2,
    (BUNDLE_LIMITS[2][0] + BUNDLE_LIMITS[2][1]) / 2,
)

CLUSTER_WORLD_POSITION: typing.Final[fcg.typing.Vec3f] = BUNDLE_CENTER

BUNDLE_RADIUS: typing.Final[float] = 0.25
BUNDLE_SYMMETRY: typing.Final[float] = 1
CENTROID_SAMPLE_SIZE: typing.Final[int] = 5
