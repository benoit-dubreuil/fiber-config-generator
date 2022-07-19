# TODO : Transform this module into a builder (design pattern).
import pathlib

import simulator.factory.geometry_factory.handlers as _sim_geom_handlers
import simulator.runner

import fcg.voxsim
import fcg.voxsim.fiber as _fiber


def generate_fiber_tracts(
    voxsim_geom_params: _sim_geom_handlers.GeometryInfos,
    simulation_name: str = fcg.voxsim.default.SIMULATION_NAME,
    out_dir: pathlib.Path = fcg.voxsim.default.OUT_DIR,
    singularity_conf: simulator.runner.SingularityConfig = simulator.runner.SingularityConfig(),
) -> None:
    """
    Generates the white matter phantom configured by the supplied geometry parameters.

    Parameters
    ----------
    voxsim_geom_params
        The VoxSim-specific geometry parameters.
    simulation_name
        The mnemonic name of the simulation. The generated log file has the same name as the simulation name, excluding
        the file extension. The generated phantom files are prefixed with the simulation name.
    out_dir
        The directory into which the generated white matter phantoms files and directories will be saved. For
        simplicity, it is usually the root output directory of all the other generated files.
    singularity_conf
        The singularity configuration which defines where the SingularityCE resources are.

    Returns
    -------
    None

    """
    simulation: simulator.runner.SimulationRunner = simulator.runner.SimulationRunner(singularity_conf)

    simulation.generate_phantom(
        run_name=simulation_name,
        phantom_infos=voxsim_geom_params,
        output_folder=out_dir,
        output_nifti=_fiber.const.GENERATE_NIFTI,
    )
