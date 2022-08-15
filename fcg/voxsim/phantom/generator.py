# TODO : Transform this module into a builder (design pattern).

import pathlib

import simulator.factory.geometry_factory.handlers as _sim_geom_handlers
import simulator.runner

import fcg.voxsim

from . import const as _const


def generate_fiber_tracts(
    voxsim_geom_params: _sim_geom_handlers.GeometryInfos,
    root_out_dir: pathlib.Path = fcg.voxsim.default.ROOT_OUT_DIR,
    simulation_name: str = fcg.voxsim.default.SIMULATION_NAME,
    singularity_conf: simulator.runner.SingularityConfig = simulator.runner.SingularityConfig(),
) -> int:
    """Generates the white matter phantom configured by the supplied geometry parameters.

    Parameters
    ----------
    voxsim_geom_params
        The VoxSim-specific geometry parameters.
    simulation_name
        The mnemonic name of the simulation. The generated log file has the same name as the simulation name, excluding
        the file extension. The generated phantom files are prefixed with the simulation name.
    root_out_dir
        The directory into which the generated white matter phantoms files and directories will be saved. For
        simplicity, it is usually the root output directory of all the other generated files.
    singularity_conf
        The singularity configuration which defines where the SingularityCE resources are.

    Returns
    -------
    int
        The returncode of the phantom generation. ``0`` if successfull, ``> 0`` otherwise.

    """
    simulation: simulator.runner.SimulationRunner = simulator.runner.SimulationRunner(singularity_conf)

    returncode: int = simulation.generate_phantom(
        run_name=simulation_name,
        phantom_infos=voxsim_geom_params,
        output_folder=root_out_dir,
        output_nifti=_const.GENERATE_NIFTI,
    )

    return returncode
