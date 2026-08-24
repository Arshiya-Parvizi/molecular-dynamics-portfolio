# Molecular Dynamics Analysis

This directory contains selected processed outputs from an atomistic molecular dynamics study of thymol and structurally related derivatives interacting with lipid membranes.

The purpose of this directory is to provide representative scientific data rather than complete simulation trajectories.

Selected GROMACS `.xvg` outputs are retained so that the accompanying Python workflows can be reproduced and inspected.

---

## Analysis Overview

| Analysis | Main Question | Data Directory | Portfolio Output |
|---|---|---|---|
| **RDF** | At what distances are selected molecular groups preferentially found relative to one another? | `rdf/` | RDF figures and peak analysis |
| **Hydrogen bonds** | How persistent are selected ligand-lipid or ligand-water interactions? | `hydrogen-bonds/` | Occupancy figures and CSV summary |
| **RMSD** | How does structural deviation evolve during the analyzed trajectory? | `rmsd/` | RMSD comparison and late-window statistics |
| **Lipid order parameter** | How does lipid-tail orientational order vary along selected segments? | `order-parameters/` | S_CD profiles and CSV summary |
| **Headgroup / distribution analysis** | How are selected headgroup-related quantities spatially distributed? | `headgroup-analysis/` | Distribution comparison and peak detection |
| **Density profiles** | Where are selected components located along the bilayer-normal coordinate? | `density-profiles/` | Raw and normalized density comparisons |

---

## Why Multiple `.xvg` Files Are Included

Each `.xvg` file corresponds to a particular simulation, atom selection, molecular group, or structural observable.

Multiple files within one analysis category are intentional.

They allow different molecular questions to be examined independently without combining physically different selections into one dataset.

The original research filenames are retained wherever practical to preserve traceability to the molecular dynamics workflow.

---

# RDF

Radial distribution functions describe how the local concentration of one selected atom or group varies with distance from another reference selection.

The portfolio RDF workflow:

- reads numerical GROMACS `.xvg` data
- ignores Grace/GROMACS metadata lines
- plots `g(r)` as a function of distance
- identifies the strongest positive RDF peak
- reports the corresponding peak distance
- preserves all-zero datasets without assigning a false positive peak

A value of:

```text
g(r) > 1
```

indicates enrichment relative to the reference bulk distribution.

A strong RDF peak identifies a preferred spatial separation between the selected groups.

RDF results are **not interpreted as proof of binding by themselves**.

They should be considered together with atom identity, hydrogen bonding, density profiles, ligand position, and other structural information.

---

# Hydrogen-Bond Analysis

Hydrogen-bond files contain selected interactions involving ligand, membrane, or solvent atoms.

The portfolio scripts calculate:

- number of analyzed frames
- mean hydrogen bonds per frame
- maximum hydrogen bonds observed
- number of frames with at least one hydrogen bond
- occupancy percentage

Occupancy is defined here as:

```text
percentage of analyzed frames containing at least one hydrogen bond
```

This is useful for identifying whether a selected donor-acceptor interaction is:

- persistent
- intermittent
- rare
- absent

Different files often correspond to different atom pairs.

For this reason, a combined occupancy plot is treated as an **interaction-specific screen**, not as a simple overall ranking of compound binding strength.

Hydrogen-bond interpretation is strongest when combined with ligand localization and density information.

---

# RMSD

Root-mean-square deviation is used as a descriptive structural stability metric for selected trajectory groups.

The scripts calculate:

- number of trajectory points
- mean RMSD
- minimum RMSD
- maximum RMSD
- standard deviation
- mean RMSD over the final 20% of the trajectory
- standard deviation over the final 20%

The final 20% is used as a descriptive **late-trajectory window**.

It is not automatically assumed to represent thermodynamic equilibration.

Absolute RMSD values should only be compared directly when:

- atom selections are comparable
- reference structures are comparable
- fitting procedures are comparable

Therefore, the portfolio emphasizes trajectory behavior and late-stage fluctuation rather than labeling a system as simply "good" or "bad" from its absolute RMSD value.

---

# Lipid Order Parameter

The lipid-tail order parameter, S_CD, describes orientational ordering along selected lipid-chain segments.

The portfolio scripts report:

- number of analyzed segments
- mean S_CD
- minimum S_CD
- segment containing the minimum
- maximum S_CD
- segment containing the maximum

The profiles can also be compared across selected systems.

In general:

```text
higher S_CD -> greater orientational ordering
lower S_CD  -> greater orientational freedom
```

This should not be simplified into "higher is better" or "lower is worse."

The order parameter describes membrane organization rather than performance.

Direct numerical comparison is most meaningful when the analyzed files use comparable:

- lipid species
- lipid tails
- atom selections
- segment definitions
- indexing schemes

---

# Headgroup / Distribution Analysis

Selected headgroup-related distribution files are analyzed using global and local peak detection.

The comparison workflow reports:

- global maximum
- coordinate of the global maximum
- weighted mean coordinate
- number of positive local peaks
- strongest local peaks

For a simple single-peaked distribution, a weighted mean may provide a useful descriptive center.

For a **multimodal distribution**, however, the weighted mean may fall between physically populated regions.

In those cases, individual local peak positions and their magnitudes are more informative.

Original atom labels are retained in the repository.

P8 is used as a phosphate-region reference in the research workflow.

Other labels are not assigned a chemical identity unless that identity can be verified from the underlying molecular system or original atom selection.

---

# Density Profiles

Density profiles describe the spatial distribution of selected simulation components along the coordinate corresponding to the bilayer-normal analysis.

In the original molecular dynamics workflow, density profiles were used to examine how ligands and membrane components were distributed relative to membrane regions.

The portfolio contains two complementary approaches.

## Raw Density Comparison

`compare_density_profiles.py` preserves the original profile amplitudes.

The script reports:

- global maximum density
- coordinate of the maximum
- weighted mean coordinate
- number of positive local peaks
- strongest local peaks

Raw profiles are useful when the magnitude and shape of the original distribution are both relevant.

For multimodal or periodically split profiles, the weighted mean should be interpreted cautiously because it may fall between populated regions.

---

## Normalized Density Comparison

`compare_normalized_density.py` divides every profile by its own maximum:

```text
normalized value = original value / maximum value
```

The maximum of every normalized curve is therefore:

```text
1.0
```

This is useful when two components have very different absolute density magnitudes.

Normalization emphasizes:

- peak position
- profile shape
- spatial overlap
- multimodal structure

Normalization removes information about absolute magnitude and therefore should not be used to compare total density between components.

It is primarily a visualization tool for spatial comparison.

---

# Scientific Interpretation

No single molecular dynamics observable is treated as definitive evidence of mechanism.

The analyses are complementary:

```text
Distance
   |
   +--> Where is the ligand?
   |
Hydrogen bonding
   |
   +--> Which polar interactions may stabilize it?
   |
RDF
   |
   +--> Which spatial separations are preferred?
   |
Density
   |
   +--> How are components distributed across the membrane?
   |
Order parameter
   |
   +--> Does membrane-tail organization change?
   |
RMSD
   |
   +--> How does structural deviation evolve?
```

Interpretation is based on the combined behavior of these observables.

---

# Reproducibility

Python analysis tools are located in:

```text
scripts/
```

Generated figures are stored in:

```text
figures/
```

Machine-readable numerical summaries are stored as CSV files in the corresponding analysis directories.

Examples include:

```text
analysis/rmsd/rmsd_summary.csv
analysis/hydrogen-bonds/hbond_summary.csv
analysis/order-parameters/order_parameter_summary.csv
analysis/headgroup-analysis/headgroup_distribution_summary.csv
analysis/density-profiles/density_profile_summary.csv
```

Python dependencies are listed in:

```text
requirements.txt
```

Install them from the repository root using:

```bash
python -m pip install -r requirements.txt
```

---

# Data Availability

This repository contains selected processed analysis outputs suitable for demonstrating the analytical workflow.

Large molecular dynamics production files are intentionally excluded.

Examples include:

```text
.xtc
.trr
.tpr
.cpt
.edr
.gro
```

Selected `.xvg` files are included because they are small, human-readable analysis outputs that allow the Python workflows to be demonstrated without distributing complete trajectories.

---

# Portfolio Scope

The Python tools in this repository were developed as reproducibility and portfolio extensions around selected molecular dynamics analysis outputs.

They are not presented as the original scripts used to generate every result in the thesis.

Their purpose is to demonstrate:

- scientific programming
- analysis automation
- reproducible plotting
- numerical summarization
- data interpretation
- Git-based research organization