# Research

The goal of the project Fiber Config Generator is to create a 3D white matter fiber crossing simulator to generate
synthetic data in order to validate our new algorithms for processing of light sheet microscopy data. To do so, the
project was divided into two parts : identify potential software libraries to delegate the white matter phantom
generation to and single out one according to predefined selection criteria (1), and develop an application program that
utilizes the selected software library (2).
The [first part](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/) was achieved in the course "initation to
research" that preceeded this internship, back in the winter 2022 academic term. The [second part](/README.md) is the
objective of this internship, which takes place in the summer 2022 academic term.


## Phantom generator

In the first part of the project, as expressed in
the [final report](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/blob/main/report/2022_inf6200_benoit_dubreuil.pdf)'
s results, the software library [Simulation Generator](https://github.com/AlexVCaron/voxsim) is singled out as the one
that is best suited for the project's needs of automation capability, ergonomics, functional independence and being
coded in Python. Those requirements sufficed the project's goal at the time, as the LINUM team lacked firsthand
experience with third-party white matter phantom simulation softwares. However, as we patched, fixed and modernized
Simulation Generator through a custom GitHub [fork](https://github.com/benoit-dubreuil/voxsim), the amount of
complications encountered and the required efforts to mend them increased monumentally. After careful deliberation, it
was decided to abandon Simulation Generator becaused of critical bugs, and its utility does not fit with the project's
goal, especially since the main purpose of that tool is to simulate diffusion MRI (DWI) signals on generated fiber
bundles. Simultaneously, stricter requirements and more specific to the fields of tractography and biomedical microscopy
were defined. Thenceforth, in order to delegate the white matter phantom generation to an external library, in addition
to the preceeding general requirements, it is imperative that it is completely accessible and open to modifications, and
that it parameterizes and allows its users to control the axon distribution, neural morphology and biological neural
network. Thus, Simulation Generator is incompatible with the new sine quibus non.

TODO : Detailed explications of what is wrong.

TODO, reuse : Its strong cohesion with [MITK Fiberfox](https://docs.mitk.org/2018.04/org_mitk_views_fiberfoxview.html)
pertains to its DWI roots

TODO, reuse :
In
the [final report](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/blob/main/report/2022_inf6200_benoit_dubreuil.pdf)
of the course "initation to research" back in the winter 2022 term that preceeded this internship,
the [Simulation Generator](https://github.com/AlexVCaron/voxsim) Python library was singled out as the software that
suited our needs of automation capability, ergonomics, functional independence and being coded in Python. Since then,
our requirements have become stricter and more specific to the fields of tractography and biomedical microscopy.
Thenceforth, in order to delegate the white matter phantom generation to an external library, it is imperative that it
parameterizes and allows its users to control the axon distribution, neural morphology and biological neural network.

TODO :

- Futur fiberfox/voxsim/simgenerator incertain, bug ou manque de feature, ne supporte pas la division d’axone en
  sous-axones (1 neurone = 1 chemin), outils pour l’IRM donc calcul des trucs dont on n'a pas besoin
- Répartition de neurones intra amas avec AI + tracto dans lsm, soct
- Configuration d’amas avec : bibliothèque de géométrie (e.g. CGAL ou jeux video) inspiré de fiberfox avec les ellipses,
- Dépôt public, python (avec dépendances bien supportées et documentées)
