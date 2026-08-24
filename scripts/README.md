# Python Analysis Scripts

This directory contains Python tools developed to make selected molecular dynamics analyses easier to reproduce, visualize, and compare.

The original trajectory analysis workflow relied primarily on GROMACS and molecular visualization tools.

The Python scripts in this repository are **portfolio and reproducibility extensions** that process selected GROMACS `.xvg` outputs and generate figures and numerical summaries.

Run all commands from the repository root.

---

## Requirements

The current scripts require:

- Python 3
- Matplotlib

Install the required package using:

```bash
python -m pip install -r requirements.txt
```

---

# RDF Analysis

## `plot_rdf.py`

Reads a GROMACS radial distribution function `.xvg` file and generates a PNG figure.

The script:

- ignores metadata lines beginning with `#` or `@`
- reads distance and `g(r)` values
- identifies the maximum positive RDF value
- reports the corresponding peak distance
- handles zero-valued datasets without forcing a false peak
- generates a publication-style plot

Example:

```bash
python scripts/plot_rdf.py analysis/rdf/RDF_THYM_2_P8.xvg
```

Example terminal output:

```text
Maximum g(r): 21.712
Peak distance: 0.468 nm
```

Generated figure:

```text
figures/RDF_THYM_2_P8.png
```

A different RDF file can be analyzed simply by changing the input path.

Example:

```bash
python scripts/plot_rdf.py analysis/rdf/RDF_THYM_2_P9.xvg
```

RDF peaks represent preferred spatial separations and should not automatically be interpreted as proof of binding.

---

# RMSD Analysis

## `plot_rmsd.py`

Processes an individual RMSD trajectory and generates a time-series figure.

The script reports:

- number of data points
- mean RMSD
- minimum RMSD
- maximum RMSD
- standard deviation
- mean RMSD over the final 20%
- standard deviation over the final 20%

Example:

```bash
python scripts/plot_rmsd.py analysis/rmsd/2Br_POPC_RMSD_10.xvg
```

The final 20% is treated as a descriptive late-trajectory window rather than automatically being assumed to represent equilibrium.

---

## `compare_rmsd.py`

Compares two or more RMSD files.

Example:

```bash
python scripts/compare_rmsd.py analysis/rmsd/2Br_POPC_RMSD_10.xvg analysis/rmsd/2Br_POPC_RMSD_7.xvg analysis/rmsd/RMSD_5.xvg analysis/rmsd/RMSD_6.xvg analysis/rmsd/RMSD_7.xvg
```

Generated figure:

```text
figures/rmsd_comparison.png
```

Generated summary:

```text
analysis/rmsd/rmsd_summary.csv
```

The CSV contains late-window mean RMSD and standard deviation for each analyzed file.

Absolute RMSD values should only be compared directly when the underlying atom selections and reference structures are comparable.

---

# Hydrogen-Bond Analysis

## `plot_hbonds.py`

Processes a selected GROMACS hydrogen-bond `.xvg` output.

The script reports:

- number of analyzed frames
- mean hydrogen bonds per frame
- maximum hydrogen bonds observed
- number of frames containing at least one hydrogen bond
- hydrogen-bond occupancy percentage

Example:

```bash
python scripts/plot_hbonds.py analysis/hydrogen-bonds/THYM_1_HB_OH_O10.xvg
```

Occupancy is defined as the percentage of analyzed frames in which at least one hydrogen bond is present for the selected interaction.

---

## `compare_hbonds.py`

Processes multiple hydrogen-bond files and generates a comparative occupancy figure and CSV summary.

Example:

```bash
python scripts/compare_hbonds.py analysis/hydrogen-bonds/THYM_1_HB_OH_O10.xvg analysis/hydrogen-bonds/THYM_1_HB_OH_O9.xvg
```

Generated figure:

```text
figures/hbond_occupancy_comparison.png
```

Generated summary:

```text
analysis/hydrogen-bonds/hbond_summary.csv
```

Different files may correspond to different compounds and atom selections.

The combined figure is therefore interpreted as a screen of selected molecular interactions rather than a direct ranking of overall binding strength.

---

# Lipid Order-Parameter Analysis

## `plot_order_parameter.py`

Processes a GROMACS lipid order-parameter output and plots the segmental order parameter, S_CD.

The script reports:

- number of analyzed tail segments
- mean S_CD
- minimum S_CD and its segment
- maximum S_CD and its segment

Example:

```bash
python scripts/plot_order_parameter.py analysis/order-parameters/2Br_OP_PROVA1_10.xvg
```

Generated figure:

```text
figures/2Br_OP_PROVA1_10.png
```

---

## `compare_order_parameters.py`

Compares multiple lipid order-parameter profiles.

Example:

```bash
python scripts/compare_order_parameters.py analysis/order-parameters/2Br_OP_PROVA1_10.xvg analysis/order-parameters/2_4DiBr_OP_PROVA1_3.xvg analysis/order-parameters/4Br_OP_PROVA3_5.xvg analysis/order-parameters/LIP_OP_PROVA1_3.xvg
```

Generated figure:

```text
figures/order_parameter_comparison.png
```

Generated summary:

```text
analysis/order-parameters/order_parameter_summary.csv
```

Higher S_CD values generally correspond to greater orientational ordering of the selected lipid-tail segments.

Lower values generally indicate greater orientational freedom.

Direct comparisons should be made cautiously unless lipid species, atom selections, tail definitions, and indexing schemes are comparable.

---

# Headgroup Distribution Analysis

## `compare-distribution.py`

Compares selected headgroup-related distribution `.xvg` files.

The script:

- reads numerical distribution data
- identifies the global maximum
- calculates a weighted mean coordinate
- detects positive local peaks
- ranks the strongest local peaks
- plots multiple distributions
- exports a CSV summary

Example:

```bash
python scripts/compare-distribution.py analysis/headgroup-analysis/2_4_DiBr_EG_1_P8.xvg analysis/headgroup-analysis/2_4_DiBr_EG_1_P9.xvg
```

Generated figure:

```text
figures/headgroup_distribution_comparison.png
```

Generated summary:

```text
analysis/headgroup-analysis/headgroup_distribution_summary.csv
```

For multimodal distributions, individual local peaks are generally more informative than the weighted mean coordinate.

The original atom labels are retained for traceability.

P8 is used as a phosphate-region reference in the research workflow.

Other labels are not assigned chemical identities unless they can be verified from the corresponding molecular system.

---

# Density-Profile Analysis

## `compare_density_profiles.py`

Compares selected density-profile `.xvg` outputs along the simulation coordinate corresponding to the bilayer-normal analysis.

The script:

- reads numerical GROMACS `.xvg` data
- identifies the global density maximum
- reports its coordinate
- calculates a weighted mean coordinate
- detects positive local maxima
- reports the strongest local peaks
- plots multiple profiles
- exports a CSV summary

Example:

```bash
python scripts/compare_density_profiles.py analysis/density-profiles/Br_MD_SEMI_2_L.xvg analysis/density-profiles/Br_MD_SEMI_2_W_I.xvg
```

Generated figure:

```text
figures/density_profile_comparison.png
```

Generated summary:

```text
analysis/density-profiles/density_profile_summary.csv
```

For multimodal or periodically split distributions, the weighted mean should be interpreted cautiously because it may lie between populated regions.

---

# Normalized Density Comparison

## `compare_normalized_density.py`

Compares density profiles after normalizing each profile to its own maximum.

For every profile:

```text
normalized density = density / maximum density
```

This gives each curve a maximum value of:

```text
1.0
```

The normalization is useful when two components have very different absolute density amplitudes but their spatial positions and profile shapes need to be compared.

Example:

```bash
python scripts/compare_normalized_density.py analysis/density-profiles/2Br_EG_2_L.xvg analysis/density-profiles/2Br_EG_2_P8.xvg
```

Generated figure:

```text
figures/normalized_density_comparison.png
```

Normalized profiles emphasize:

- relative peak position
- profile shape
- spatial overlap
- multimodal structure

Normalization removes information about absolute magnitude.

The resulting plot should therefore be used for spatial comparison rather than comparison of total density.

---

# Output Organization

Generated figures are stored in:

```text
figures/
```

Generated numerical summaries are stored in the appropriate analysis directory.

Examples:

```text
analysis/rmsd/rmsd_summary.csv
analysis/hydrogen-bonds/hbond_summary.csv
analysis/order-parameters/order_parameter_summary.csv
analysis/headgroup-analysis/headgroup_distribution_summary.csv
analysis/density-profiles/density_profile_summary.csv
```

---

# Scientific Interpretation

The scripts automate processing and visualization, but interpretation still depends on the molecular context of each input file.

Important considerations include:

- atom identity
- lipid species
- membrane composition
- reference structure
- trajectory selection
- simulation stage
- coordinate definitions
- periodic boundary conditions

The scripts therefore avoid assigning unsupported molecular identities or mechanistic conclusions based only on filenames.

---

# Portfolio Scope

These Python scripts were developed to demonstrate a reproducible computational-analysis workflow around selected molecular dynamics outputs.

They showcase:

- Python scripting
- file parsing
- scientific plotting
- automated numerical summaries
- comparative analysis
- reproducible research organization

They should not be interpreted as a claim that the same scripts were used in the original thesis analysis workflow.