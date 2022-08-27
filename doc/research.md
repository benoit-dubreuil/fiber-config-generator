# Research


## Phantom generator

The goal of the project [Fiber Config Generator](/README.md) is to create a 3D white matter fiber crossing simulator to
generate synthetic data in order to validate our new algorithms for processing of light sheet microscopy data. To do so,
the project was divided into two parts : identify potential software libraries to delegate the white matter phantom
generation to and single out one according to predefined selection criteria (1), and develop an application program that
utilizes the selected software library (2).

WIP  
Back in the winter 2022 term, in the course "initation to research" that preceeded this internship as it shares the same
project,
the [final report](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/blob/main/report/2022_inf6200_benoit_dubreuil.pdf)
describes the main goal of creating a 3D white matter fiber crossing simulator to generate synthetic data in order to
validate our new algorithms for processing of light sheet microscopy data.

In
the [final report](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/blob/main/report/2022_inf6200_benoit_dubreuil.pdf)
of the course "initation to research" back in the winter 2022 term that preceeded this internship,
the [Simulation Generator](https://github.com/AlexVCaron/voxsim) Python library was singled out as the software that
suited our needs of automation capability, ergonomics, functional independence and being coded in Python. Since then,
our requirements have become stricter and more specific to the fields of tractography and biomedical microscopy.
Thenceforth, in order to delegate the white matter phantom generation to an external library, it is imperative that it
parameterizes and allows its users to control the axon distribution, neural morphology and biological neural network.

TODO : Simulation Generator does not meet the new requirements

TODO : [fork](https://github.com/benoit-dubreuil/voxsim) of Simulation Generator
