# Conception

## Simulation Generator parameters

Unimportant or irrelevant Simulation Generator parameters are defined as constants and thus have no value in being
parameterized for this application. Also, Simulation Generator offers a lot of flexibility with a multitude of
parameters, many of which are interconnected. In order to reduce the noise and focus on more abstract concepts, some of
Simulation Generator's general parameters are defined as conventions (constants).


## Conventions

###### The physical space is the 3D space

Supporting both the 2D and 3D would significantly increase the complexity of the parameterization.


###### There is only one neural cluster and it contains all white matter bundles;

The goal of the project is to generate specific white matter bundles, perhaps a few of them together, in order to test
new algorithms related to a novel microscope and prospects for usability with future microscopes. Thus, there is no need
to generate multiple white matter clusters which themselves are comprised of multiple bundles, as the quantity of
produced data would simply be excessive for the goal.


- the voxel size in milimeters is `(1, 1, 1)`;
- the Simulation Generator geometry configuration files are prefixed with `geom_`;
- the generated white matter phantom subdirectory is named `phantom/`;
    - the generated white matter bundles are prefixed with the name of the simulation, like so : `name_`;
    - the bundles are then prefixed with the word `phantom_`;
