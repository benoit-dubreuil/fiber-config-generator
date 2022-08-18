import typing

import fcg.typing

from .. import const as _geom_const

BUNDLE_N_FIBERS: typing.Final[int] = 800
BUNDLE_CENTER: typing.Final[fcg.typing.Vec3f] = (0.5, 0.5, 0.5)
BUNDLE_LIMITS: typing.Final[list[list[float]]] = [[0, 1], [0, 1], [0, 1]]

WORLD_CENTER: typing.Final[fcg.typing.Vec3f] = (
    _geom_const.MRI_RESOLUTION[0] / 2,
    _geom_const.MRI_RESOLUTION[1] / 2,
    _geom_const.MRI_RESOLUTION[2] / 2,
)

BUNDLE_RADIUS: typing.Final[float] = 0.25
BUNDLE_SYMMETRY: typing.Final[float] = 1
CENTROID_SAMPLE_SIZE: typing.Final[int] = 500
BASE_ANCHORS: typing.Final[list[fcg.typing.Vec3f]] = [
    (0.0, 0.0, 0.0),
    (0.25, 0.1, 0.0),
    (0.5, 0.5, 0.0),
    (0.75, 0.1, 0.0),
    (1.0, 0.0, 0.0),
]
