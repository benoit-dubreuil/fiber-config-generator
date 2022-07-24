import typing

import fcg.typing
import fcg.voxsim.geom.const

N_POINT_PER_CENTROID: typing.Final[int] = 5

WORLD_CENTER: typing.Final[fcg.typing.Vec3f] = (
    fcg.voxsim.geom.const.MRI_RESOLUTION[0] / 2,
    fcg.voxsim.geom.const.MRI_RESOLUTION[1] / 2,
    fcg.voxsim.geom.const.MRI_RESOLUTION[2] / 2,
)

BUNDLE_RADIUS: typing.Final[float] = 4
BUNDLE_SYMMETRY: typing.Final[float] = 1
BUNDLE_N_FIBERS: typing.Final[int] = 1000
BUNDLE_LIMITS: typing.Final[typing.List[typing.List[float]]] = [[0, 1], [0, 1], [0, 1]]
BUNDLE_CENTER: typing.Final[fcg.typing.Vec3f] = (0.5, 0.5, 0.5)

BASE_ANCHORS: typing.Final[typing.List[fcg.typing.Vec3f]] = [
    (0.5, -0.3, 0.5),
    (0.5, -0.2, 0.5),
    (0.5, -0.1, 0.5),
    (0.5, 0.0, 0.5),
    (0.5, 0.1, 0.5),
    (0.5, 0.2, 0.5),
    (0.5, 0.3, 0.5),
    (0.5, 0.4, 0.5),
    (0.5, 0.5, 0.5),
    (0.5, 0.6, 0.5),
    (0.5, 0.7, 0.5),
    (0.5, 0.8, 0.5),
    (0.5, 0.9, 0.5),
    (0.5, 1.1, 0.5),
    (0.5, 1.2, 0.5),
    (0.5, 1.3, 0.5),
]
