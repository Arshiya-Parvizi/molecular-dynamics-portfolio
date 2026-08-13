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
