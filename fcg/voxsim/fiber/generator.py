# TODO : Transform this module into a builder (design pattern).
import pathlib

import simulator.factory.geometry_factory.handlers as _sim_geom_handlers
import simulator.runner

import fcg.voxsim
import fcg.voxsim.fiber as _phantom


def generate_fiber_tracts(
    voxsim_geom_params: _sim_geom_handlers.GeometryInfos,
    simulation_name: str = fcg.voxsim.default.SIMULATION_NAME,
    out_dir: pathlib.Path = fcg.voxsim.default.OUT_DIR,
    singularity_conf: simulator.runner.SingularityConfig = simulator.runner.SingularityConfig(),
) -> None:
    simulation: simulator.runner.SimulationRunner = simulator.runner.SimulationRunner(singularity_conf)

    simulation.generate_phantom(
        run_name=simulation_name,
        phantom_infos=voxsim_geom_params,
        output_folder=out_dir,
        output_nifti=_phantom.const.GENERATE_NIFTI,
    )
