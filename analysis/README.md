# Molecular Dynamics Trajectory Analysis

This directory contains selected analysis outputs generated during my MSc molecular dynamics research on thymol and thymol-derived compounds interacting with model lipid membranes.

The analyses were performed primarily using GROMACS trajectory-analysis tools. Multiple atom selections and molecular groups were evaluated for each type of analysis because different atoms probe different aspects of ligand–membrane interactions.

The `.xvg` files retained in this repository are selected research outputs used to demonstrate the analysis workflow. Large trajectories and raw simulation files are intentionally excluded.

## Membrane Systems

Two membrane environments were investigated:

* **POPC membrane** — neutral membrane model
* **POPE/POPG membrane** — negatively charged bacterial-like membrane model

The compounds investigated were:

* Thymol
* Carvacrol
* Thymol acetate
* 2-Bromothymol
* 4-Bromothymol
* 2,4-Dibromothymol

## Analysis Categories

### Radial Distribution Functions — `rdf/`

Radial distribution function (RDF) analysis was used to investigate the spatial relationship between selected ligand atoms and specific atoms or groups within the lipid membrane.

Multiple RDF calculations were performed using different lipid atoms because each selection can provide information about a different region or interaction within the membrane.

The filenames preserve the original atom selections used during the analysis.

Examples include RDF calculations involving:

* P8/P9-related selections
* O14
* O15
* O33
* O35
* O36
* O38

The exact interpretation of an atom label depends on the lipid and simulation system from which the analysis was generated.

---

### Hydrogen-Bond Analysis — `hydrogen-bonds/`

Hydrogen-bond analysis was used to investigate polar interactions between the compounds, lipid headgroups, and in some cases interfacial water.

For compounds containing a free phenolic hydroxyl group, the OH group can act as an important hydrogen-bond donor at the membrane interface.

Different donor and acceptor atom selections were analyzed separately. The repository therefore contains several hydrogen-bond output files rather than a single general hydrogen-bond calculation.

Examples include interactions involving ligand hydroxyl groups and selected lipid oxygen or nitrogen atoms, as well as water-mediated interactions.

---

### Lipid Order Parameters — `order-parameters/`

Lipid acyl-chain organization was evaluated using order-parameter analysis.

The deuterium order parameter, S_CD, provides information about lipid-tail organization and can reveal whether ligand interaction at the membrane surface propagates into changes in the hydrophobic region of the bilayer.

Different lipid species and carbon selections were evaluated depending on the membrane system.

These analyses were performed using GROMACS order-parameter tools and dedicated atom/index selections.

---

### Headgroup Analysis — `headgroup-analysis/`

The polar lipid headgroup region was investigated using selected structural atom distributions and distances.

One important headgroup descriptor used in the research was the distance involving the lipid phosphate region. In the thesis notation, P8 represents a phosphate atom used as a membrane-headgroup reference.

P8/P9-related output files are retained with their original research filenames so that they can later be linked to the corresponding topology/index definitions.

This analysis was used to investigate ligand-associated changes in the organization of the membrane interface.

---

### RMSD — `rmsd/`

Root-mean-square deviation (RMSD) calculations were performed on selected systems as part of trajectory assessment.

The included `.xvg` outputs provide examples of the structural evolution observed during molecular dynamics simulations.

Multiple RMSD files correspond to different simulation systems or independent trajectories.

---

### Density Profiles — `density-profiles/`

Mass-density profiles were used to determine the position of compounds and membrane components relative to the lipid bilayer.

The profiles were calculated along the **z-axis**, corresponding to the membrane-normal direction.

Density distributions of selected components such as:

* ligand
* lipid headgroup region
* lipid membrane
* water

can be compared to determine whether a compound remains near the membrane interface or penetrates more deeply toward the hydrophobic core.

Representative density-profile data will be added to this directory separately.

## Why Multiple Files Are Included

The presence of several files for a single analysis type is intentional.

Molecular dynamics analysis often requires examining multiple atom selections rather than treating the membrane or ligand as a single object.

For example, separate RDF or hydrogen-bond calculations can be used to investigate interactions with different functional groups or regions of the lipid headgroup.

Therefore, these files represent different molecular questions and atom selections rather than redundant copies of the same calculation.

## File Naming

Most filenames preserve the original names used during the research workflow.

Typical elements include:

* compound abbreviation
* simulation or replicate number
* analysis type
* selected atom or molecular group

Examples:

`rdf_2_4DiBr_2_O15.xvg`

indicates an RDF analysis involving the 2,4-dibromothymol system and an O15 atom selection.

`CARV_HB_3_OH_N4.xvg`

indicates a hydrogen-bond analysis involving a carvacrol system and selected OH/N4 groups.

The original filenames are retained to preserve traceability to the simulation workflow.

## Data Format

Most numerical outputs in this directory use the GROMACS `.xvg` format.

These files generally contain:

* metadata generated by GROMACS
* axis information
* series labels where available
* numerical analysis data

The `.xvg` files can be viewed using Grace-compatible software or parsed programmatically.

A later part of this portfolio will demonstrate how these outputs can be imported, processed, and visualized reproducibly using Python.

## Data Availability

This repository contains selected analysis-level data only.

Large or raw simulation files such as trajectories, checkpoint files, run-input files, and complete simulation datasets are not distributed through this public portfolio.

The purpose of the repository is to demonstrate the molecular dynamics workflow, analysis strategy, scientific interpretation, and development of reproducible computational analysis skills.
