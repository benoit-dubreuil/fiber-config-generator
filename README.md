# Fiber Config Generator

## White matter fiber tracts configuration generator


## INM5803 – Stage d'informatique III

### Été 2022

Développé par Benoît Dubreuil sous la supervision du professeur-superviseur Joël Lefebvre du LINUM au cours de la session d'été 2022 à l'UQÀM pour un stage COOP (INM5803).


## Workflows

### Dependent Issues

The [Dependent Issues](https://github.com/z0al/dependent-issues) GitHub action and actual GitHub workflow allows issues and PRs dependency management through keywords in
descriptions.

The keywords are `depends on` and `blocked by`, according to the configuration.
Also, the Dependent Issues GitHub action labels issues and PRs that are dependent on others with the label `dependent`, according to the configuration.
Finally, the GitHub action adds itself to the list of status checks required to pass before merging PRs.