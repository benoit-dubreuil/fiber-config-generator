# TODO : Transform this module into a builder (design pattern).
import pathlib

import fcg.voxsim
import fcg.voxsim.phantom as _phantom
from simulator.factory.geometry_factory.handlers import GeometryInfos
from simulator.runner import SimulationRunner


def generate_fiber_tracts(
    voxsim_geom_params: GeometryInfos,
    out_dir: pathlib.Path = fcg.voxsim.default.OUT_DIR
) -> None:
    # TODO : Supply SingularityConfig to SimulationRunner with custom attribute values
    simulation: SimulationRunner = SimulationRunner()

    simulation.generate_phantom(fcg.voxsim.default.RUN_NAME,
                                voxsim_geom_params,
                                out_dir,
                                output_nifti=_phantom.default.GENERATE_NIFTI)
