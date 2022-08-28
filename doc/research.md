# Research

The goal of the project Fiber Config Generator is to create a 3D white matter fiber crossing simulator to generate
synthetic data in order to validate our new algorithms for processing of light sheet microscopy data. To do so, the
project was divided into two parts : identify potential software libraries to delegate the white matter phantom
generation to and single out one according to predefined selection criteria (1), and develop an application program that
utilizes the selected software library (2).
The [first part](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/) was achieved in the course "initiation to
research" that preceded this internship, back in the winter 2022 academic term. The [second part](/README.md) is the
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
was decided to abandon Simulation Generator because of critical bugs, and its utility does not fit with the project's
goal, especially since the main purpose of that tool is to simulate diffusion MRI (DWI) signals on generated fiber
bundles. Simultaneously, stricter requirements and more specific to the fields of tractography and biomedical microscopy
were defined. Thenceforth, in order to delegate the white matter phantom generation to an external library, in addition
to the preceding general requirements, it is imperative that it is completely accessible and open to modifications, and
that it parameterizes and allows its users to control the axon distribution, neural morphology and biological neural
network. Thus, Simulation Generator is incompatible with the new sine quibus non.


### Inadequacies

- Its strong cohesion with [MITK Fiberfox](https://docs.mitk.org/2018.04/org_mitk_views_fiberfoxview.html)
  pertains to its DWI roots. It is impossible to truly dissociate the brain white matter phantom from its DWI
  simulation.
- The generated geometric shape is unpredictable. See the V-shaped [example](#examplev-shaped-bundle) below.


#### Example&ThinSpace;:&emsp13;V-shaped bundle

According to
voXSim "[concepts](https://github.com/AlexVCaron/voxsim/blob/76ca69902459e0d3dc830ea14635dd38e2951dd2/.cache/doc/concepts.rst)"
documentation page, it should be possible to generate a fiber bundle in a V shape with only three anchors.

```python
# V shape with 3 anchors
anchors = [
    (0.0, 0.0, 0.0),
    (0.5, 0.8, 0.0),
    (1.0, 0.0, 0.0),
]
```

![Erroneous V shape with 3 anchors](img/sim_gen__v_shape__bad.png)

Unfortunately, through trial and error, generating a simple V-shaped bundle with three anchors seems impossible. The
image above is an example of the resulting output.

```python
# V shape with 5 anchors
anchors = [
    (0.0, 0.0, 0.0),
    (0.25, 0.15, 0.0),
    (0.5, 0.5, 0.0),
    (0.75, 0.15, 0.0),
    (1.0, 0.0, 0.0),
]
```

![Satisfactory V shape with 3 anchors](img/sim_gen__v_shape__good.png)

It is possible to generate a simple V-shaped bundle with more than three anchors. However, as seen in the image above,
the anchors spatial positions offer next to no control over the actual shape of the resulting bundle.

TODO : Detailed explications of what is wrong.

TODO : The critical bug is due to uncertainty and guessing of some variables.

TODO : Lack of features : Simulation Generator does not offer a possibility to modify the tension, bias and continuity
of the centroid, as described in
its [concepts](https://github.com/AlexVCaron/voxsim/blob/76ca69902459e0d3dc830ea14635dd38e2951dd2/.cache/doc/concepts.rst)
documentation. Also, it seems it only affects the DWI simulation.

TODO : voXSim is an amelioration of Fiberfox which, contrarily to the latter, allows its users to control the generation
through the command-line interface (CLI). Also, Simulation Generator offers a high level Python API to voXSim. There are
no equivalents for Fiberfox.

TODO, reuse :
In
the [final report](https://github.com/linum-uqam/inf6200-h2022-benoit-dubreuil/blob/main/report/2022_inf6200_benoit_dubreuil.pdf)
of the course "initiation to research" back in the winter 2022 term that preceded this internship,
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
