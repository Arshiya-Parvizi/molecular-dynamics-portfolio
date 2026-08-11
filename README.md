# Molecular Dynamics & Computational Biology & Biotechnology Portfolio

## About This Portfolio

This repository presents selected computational work developed during my MSc research in Biotechnology, with a focus on molecular dynamics simulations, membrane biophysics, and analysis of small-molecule interactions with lipid membranes.

The main case study investigates the interaction of thymol-derived compounds with model lipid membranes using atomistic molecular dynamics simulations performed with GROMACS.

The repository documents the simulation workflow, trajectory analyses, visualization approaches, and selected analysis outputs used during the research.

---

## Research Case Study

### Molecular Dynamics of Thymol Derivatives in Model Membranes

The study investigated six thymol-derived compounds:

* Thymol
* Carvacrol
* 2-Bromothymol
* 4-Bromothymol
* 2,4-Dibromothymol
* Thymol acetate

Two membrane models were investigated:

**Neutral membrane**

* 128 POPC lipids

**Negatively charged membrane**

* 90 POPE lipids
* 38 POPG lipids

Simulation systems also contained SPC water and the required ions.

For each compound, multiple independent systems were constructed to investigate membrane self-assembly and compound–membrane interactions.

---

## Molecular Dynamics Workflow

The simulation workflow involved:

1. Construction of simulation boxes
2. Addition of compound, lipids, water, and ions
3. Minimum-bias/self-assembly simulations
4. Multiple stages of energy minimization
5. Anisotropic annealing/equilibration
6. Semi-isotropic annealing/equilibration
7. Structural inspection and quality control
8. Production molecular dynamics simulations
9. Trajectory analysis
10. Visualization and interpretation of simulation results

The molecular dynamics simulations were performed using GROMACS. Computationally intensive simulations were carried out using the CINECA high-performance computing facility in Bologna.

---

## Simulation System Preparation

Simulation boxes were constructed with dimensions of approximately:

`9.0 × 9.0 × 9.0`

Each system contained:

* One molecule of the investigated compound
* Approximately 7500 SPC water molecules
* A membrane lipid composition appropriate to the model
* Counterions/ions according to the system charge

For the neutral membrane system, 128 POPC molecules were used.

For the negatively charged membrane system, 90 POPE and 38 POPG molecules were used.

Multiple independent systems were prepared for each compound to provide repeated simulations and allow structural quality assessment.

---

## Simulation Quality Control

An important part of the workflow was visual inspection of the self-assembled membrane systems.

Simulation boxes were inspected and, when necessary, centered for visualization and analysis.

Systems showing poorly formed, unstable, or strongly disordered membrane structures were discarded and reconstructed from the beginning.

This quality-control step was used to ensure that the systems selected for subsequent analysis showed acceptable membrane organization.

---

## Trajectory Analysis

Several analyses were performed on the molecular dynamics trajectories, including:

### RMSD

Root-mean-square deviation analysis was used to examine structural changes throughout the simulations.

### Radial Distribution Functions

Radial distribution functions were used to investigate spatial relationships between selected atoms/groups.

The analysis included specific oxygen atoms such as O15 in POPE/POPG systems, as well as P8/P9-related distributions.

### Density Profiles

Density profiles were calculated along the **Z axis**, corresponding to the membrane-normal direction used in the analysis.

### Hydrogen Bond Analysis

Hydrogen-bond analyses were performed between selected molecular groups to investigate compound–membrane interactions.

### Lipid Order Parameters

Lipid order parameters were calculated for selected lipid carbon atoms using GROMACS analysis tools and custom index groups.

### P8/P9 Distributions

The distribution of P8 and P9 was analyzed as part of the structural characterization of the simulated membrane systems.

---

## Visualization

Simulation structures and trajectories were inspected using:

* **VMD**
* **ChimeraX**

These tools were used to examine membrane organization, molecular positioning, distances, and structural changes during the simulations.

---

## Computational Tools

| Tool       | Application                                            |
| ---------- | ------------------------------------------------------ |
| GROMACS    | Molecular dynamics simulations and trajectory analysis |
| Linux      | Simulation and command-line workflow                   |
| CINECA HPC | High-performance molecular dynamics simulations        |
| VMD        | Molecular visualization and trajectory inspection      |
| ChimeraX   | Molecular structure visualization                      |
| Python     | Planned/reproducible analysis extensions               |

---

## Repository Structure

```text
molecular-dynamics-portfolio/
│
├── README.md
│
├── docs/
│   ├── simulation-workflow.md
│   └── analysis-methods.md
│
├── analysis/
│   ├── rdf/
│   ├── hydrogen-bonds/
│   ├── order-parameters/
│   ├── density-profiles/
│   └── rmsd/
│
├── figures/
│
├── notebooks/
│
└── scripts/
```

---

## Data Availability

Only selected and representative analysis files are included in this portfolio.

Large molecular dynamics trajectories and original simulation datasets are not included in the public repository.

The purpose of this repository is to demonstrate the computational workflow, analysis methods, and scientific reasoning developed during the research project.

---

## Background

This portfolio is based on computational work conducted as part of my MSc research in Biotechnology, focusing on molecular dynamics simulations and the interaction of thymol-derived compounds with model lipid membranes.
