from pathlib import Path
import sys
import matplotlib.pyplot as plt


# Check that the user provided an input file
if len(sys.argv) < 2:
    print("Usage: python scripts/plot_rdf.py <rdf_file>")
    sys.exit(1)

# Input RDF file from the command line
input_file = Path(sys.argv[1])

# Output figure name will match the input filename
output_file = Path("figures") / f"{input_file.stem}.png"


# Lists to store numerical data
distance = []
rdf = []


# Read the .xvg file
with input_file.open("r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        # Skip GROMACS/Grace metadata
        if line.startswith("#") or line.startswith("@"):
            continue

        values = line.split()

        distance.append(float(values[0]))
        rdf.append(float(values[1]))


# Find the maximum RDF value and its distance
max_rdf = max(rdf)
max_index = rdf.index(max_rdf)
peak_distance = distance[max_index]

print(f"Maximum g(r): {max_rdf:.3f}")
print(f"Peak distance: {peak_distance:.3f} nm")


# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(distance, rdf)

# Reference line for uniform distribution
plt.axhline(y=1, linestyle="--", linewidth=1)

# Mark the RDF peak only when a positive peak exists
if max_rdf > 0:
    plt.scatter(peak_distance, max_rdf)

    plt.annotate(
        f"Peak: {peak_distance:.3f} nm\ng(r) = {max_rdf:.2f}",
        xy=(peak_distance, max_rdf),
        xytext=(peak_distance + 0.15, max_rdf * 0.8),
        arrowprops=dict(arrowstyle="->")
    )
else:
    print("No positive RDF peak found in this dataset.")
plt.xlabel("Distance (nm)")
plt.ylabel("g(r)")
plt.title(f"Radial Distribution Function: {input_file.stem}")

plt.tight_layout()

# Make sure figures folder exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Save and show
plt.savefig(output_file, dpi=300)
plt.show()