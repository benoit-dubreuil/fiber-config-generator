# Conception

## VoxSim parameters

Unimportant or irrelevant VoxSim parameters are defined as constants and thus have no value in being parameterized for
this application. Also, Simulation Generator offers a lot of flexibility with a multitude of parameters, many of which
are interconnected. In order to reduce the noise and focus on more abstract concepts, some of Simulation Generator's
general parameters are defined as conventions (constants).


## Conventions

By convention,

- the physical space is the 3D space;
- there is only one neural cluster and it contains all white matter bundles;
- the voxel size in milimeters is `(1, 1, 1)`;
- the Simulation Generator geometry configuration files are prefixed with `geom_`;
- the generated white matter phantom subdirectory is named `phantom/`;
    - the generated white matter bundles are prefixed with the name of the simulation, like so : `name_`;
    - the bundles are then prefixed with the word `phantom_`;
