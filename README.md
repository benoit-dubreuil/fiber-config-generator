# Fiber Config Generator

## White matter fiber tracts configuration generator


## INM5803 – Stage d'informatique III

### Été 2022

Développé par Benoît Dubreuil sous la supervision du professeur-superviseur Joël Lefebvre du LINUM au cours de la session d'été 2022 à l'UQÀM pour un stage COOP (INM5803).


## GitHub workflows

### Create Issue Branch

The [Create Issue Branch](https://github.com/robvanderleek/create-issue-branch) GitHub Action and actual GitHub workflow automates the creation of issue branches after assigning an
issue.

Its workflow is located at `.github/workflows/create-issue-branch.yml`.
Its configuration is located at `.github/issue-branch.yml`.

The issue branches created are named with the following
pattern: `${lowercased label}/issue-${number}/${lowercased issue title in which unsafe characters are replaced by the character "-"}`.

The supported labels are `bug`, and `feature`, `doc` and `QA`.
As an exception, the `bug` label actually generates the prefix `fix` in created branches.
Any other label exclude the assigned issue from automatic branch creation.

The Create Issue Branch GitHub Action also automatically closes issue which its PR was merged to the `dev/` branch.

The GitHub Action creates an open draft PR when an issue is assigned and labelled correctly.
The issue's description and labels are copied to the automatically created PR.


### Dependent Issues

The [Dependent Issues](https://github.com/z0al/dependent-issues) GitHub Action and actual GitHub workflow allows issues and PRs dependency management through keywords in
descriptions.

Its workflow and configuration is located at `.github/workflows/dependent-issues.yml`.

The keywords are `depends on` and `blocked by`, according to the configuration.
Also, the Dependent Issues GitHub Action labels issues and PRs that are dependent on others with the label `dependent`, according to the configuration.
Finally, the GitHub Action adds itself to the list of status checks required to pass before merging PRs.