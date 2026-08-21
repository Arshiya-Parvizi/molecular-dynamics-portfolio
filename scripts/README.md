# Python Analysis Scripts

This directory contains Python tools developed to make selected molecular dynamics analyses from my MSc research more reproducible and easier to visualize.

The original trajectory analyses were performed using GROMACS. These Python scripts are portfolio extensions that read selected GROMACS output files and generate clean figures and quantitative summaries.

## RDF Plotting

### `plot_rdf.py`

This script reads a GROMACS radial distribution function (`.xvg`) file and generates a PNG plot.

The script:

* reads numerical data from a GROMACS `.xvg` file
* ignores GROMACS/Grace metadata lines beginning with `#` or `@`
* extracts distance and radial distribution function values
* identifies the maximum RDF value
* reports the distance at which the maximum occurs
* marks the peak on the generated plot when a positive peak is present
* correctly handles datasets containing no positive RDF values
* saves the resulting figure in the `figures/` directory

## Usage

Run the script from the repository root:

```bash
python scripts/plot_rdf.py analysis/rdf/RDF_THYM_2_P8.xvg
```

The script will print information such as:

```text
Maximum g(r): 21.712
Peak distance: 0.468 nm
```

and generate:

```text
figures/RDF_THYM_2_P8.png
```

A different RDF file can be analyzed simply by changing the input path:

```bash
python scripts/plot_rdf.py analysis/rdf/RDF_THYM_2_P9.xvg
```

This allows the same analysis code to be reused across different compounds, membrane atoms, and simulation systems.

## Requirements

The current script requires:

* Python 3
* Matplotlib

Install the required Python package with:

```bash
python -m pip install -r requirements.txt
```

## Scientific Interpretation

The radial distribution function, (g(r)), describes how the spatial probability of finding a selected atom or group varies with distance from another selected reference.

A pronounced RDF peak indicates a preferred spatial separation between the selected groups.

RDF results are interpreted together with the identity of the selected atoms and complementary molecular dynamics analyses rather than being treated as a standalone measure of binding strength.

## Development

Additional scripts will be added for other molecular dynamics analyses such as RMSD, hydrogen bonding, lipid order parameters, and density profiles.

## RMSD Analysis

### `plot_rmsd.py`

This script reads a GROMACS RMSD `.xvg` file and generates a time-series plot together with descriptive statistics.

The script reports:

* number of trajectory data points
* mean RMSD
* minimum and maximum RMSD
* RMSD standard deviation
* mean RMSD during the final 20% of the trajectory
* standard deviation during the final 20%

The final 20% is treated as a descriptive late-trajectory window rather than being automatically assumed to represent equilibrium.

Example:

```bash
python scripts/plot_rmsd.py analysis/rmsd/2Br_POPC_RMSD_10.xvg
```

### `compare_rmsd.py`

This script compares two or more RMSD trajectories using the same analysis workflow.

Example:

```bash
python scripts/compare_rmsd.py analysis/rmsd/2Br_POPC_RMSD_10.xvg analysis/rmsd/2Br_POPC_RMSD_7.xvg analysis/rmsd/RMSD_5.xvg analysis/rmsd/RMSD_6.xvg analysis/rmsd/RMSD_7.xvg
```

The script generates:

```text
figures/rmsd_comparison.png
```

and a machine-readable summary:

```text
analysis/rmsd/rmsd_summary.csv
```

The CSV contains the final-20%-trajectory mean RMSD and standard deviation for each analyzed file.

Absolute RMSD values should only be compared directly when the underlying atom selections and reference structures are comparable. The scripts therefore emphasize reproducible processing and trajectory behavior rather than assigning stability based solely on RMSD magnitude.
## Hydrogen-Bond Analysis

### `plot_hbonds.py`

This script processes selected GROMACS hydrogen-bond `.xvg` outputs and reports:

- number of analyzed frames
- mean hydrogen bonds per frame
- maximum hydrogen bonds observed in a frame
- number of frames containing at least one hydrogen bond
- hydrogen-bond occupancy percentage

Occupancy is defined here as the percentage of analyzed trajectory frames in which at least one hydrogen bond is present for the selected interaction.

### `compare_hbonds.py`

This script processes multiple atom-specific hydrogen-bond outputs and generates both a graphical occupancy comparison and a CSV summary.

Outputs:

`figures/hbond_occupancy_comparison.png`

`analysis/hydrogen-bonds/hbond_summary.csv`

Different files correspond to different compounds and atom selections. Therefore, the combined plot is interpreted as a screen of selected molecular interactions rather than a direct ranking of overall compound binding strength.
## Lipid Order-Parameter Analysis

### `plot_order_parameter.py`

This script processes GROMACS lipid order-parameter output and plots the segmental deuterium order parameter, (S_{CD}), along the selected lipid tail.

The script reports:

* number of analyzed tail segments
* mean (S_{CD})
* minimum (S_{CD}) and its segment
* maximum (S_{CD}) and its segment

Example:

```bash
python scripts/plot_order_parameter.py analysis/order-parameters/2Br_OP_PROVA1_10.xvg
```

### `compare_order_parameters.py`

This script compares multiple lipid order-parameter profiles and exports both a graphical comparison and a numerical summary.

Example:

```bash
python scripts/compare_order_parameters.py analysis/order-parameters/2Br_OP_PROVA1_10.xvg analysis/order-parameters/2_4DiBr_OP_PROVA1_3.xvg analysis/order-parameters/4Br_OP_PROVA3_5.xvg analysis/order-parameters/LIP_OP_PROVA1_3.xvg
```

Outputs:

```text
figures/order_parameter_comparison.png
analysis/order-parameters/order_parameter_summary.csv
```

Higher (S_{CD}) values generally indicate greater orientational ordering of the selected lipid-tail segments, while lower values indicate greater orientational freedom.

Profiles are interpreted primarily by their segment-by-segment shape and by differences between comparable membrane selections. Absolute values should not be ranked across systems unless the lipid species, atom selections, and indexing scheme are equivalent.

The scripts retain the original research filenames to preserve traceability to the molecular dynamics workflow.
## Headgroup Distribution Analysis

### `compare-distribution.py`

This script compares selected lipid-headgroup distribution outputs from the molecular dynamics analysis.

The script:

* reads numerical `.xvg` distribution data
* identifies the global maximum
* detects positive local peaks
* reports the strongest populated regions
* calculates a weighted mean coordinate as a descriptive statistic
* compares multiple distributions on a single figure
* exports a CSV summary

Example:

```bash
python scripts/compare-distribution.py analysis/headgroup-analysis/2_4_DiBr_EG_1_P8.xvg analysis/headgroup-analysis/2_4_DiBr_EG_1_P9.xvg
```

Outputs:

```text
figures/headgroup_distribution_comparison.png
analysis/headgroup-analysis/headgroup_distribution_summary.csv
```

For multimodal distributions, the locations and magnitudes of individual local peaks are generally more informative than the weighted mean coordinate alone.

Atom labels retain the original research nomenclature. In the thesis workflow, P8 was used as a phosphate-region headgroup reference. Other atom labels are interpreted according to the corresponding molecular system and original atom selections.
## Density-Profile Analysis

### `compare_density_profiles.py`

This script compares selected density-profile `.xvg` outputs along the simulation coordinate corresponding to the bilayer-normal analysis.

The script:

- reads numerical GROMACS `.xvg` data
- identifies the global density maximum
- detects positive local maxima
- reports the strongest local peaks
- calculates a weighted mean coordinate as a descriptive statistic
- plots multiple profiles together
- exports a numerical CSV summary

Example:

```bash
python scripts/compare_density_profiles.py analysis/density-profiles/Br_MD_SEMI_2_L.xvg analysis/density-profiles/Br_MD_SEMI_2_W_I.xvg
## Normalized Density Comparison

### `compare_normalized_density.py`

This script compares multiple density profiles after normalizing each profile to its own maximum value.

This is useful when the profiles have very different absolute magnitudes but need to be compared by:

- peak position
- profile shape
- relative spatial distribution

Example:

```bash
python scripts/compare_normalized_density.py analysis/density-profiles/2Br_EG_2_L.xvg analysis/density-profiles/2Br_EG_2_P8.xvg