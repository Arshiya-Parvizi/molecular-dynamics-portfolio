from pathlib import Path
import sys
import csv
import matplotlib.pyplot as plt


# Require at least two distribution files
if len(sys.argv) < 3:
    print(
        "Usage: python scripts/compare-distribution.py "
        "<file1> <file2> [file3 ...]"
    )
    sys.exit(1)


# Convert command-line filenames into Path objects
input_files = [Path(filename) for filename in sys.argv[1:]]


# Store numerical summaries for CSV output
summary_results = []


# Function for finding local peaks
def find_local_peaks(x_values, y_values):
    peaks = []

    # Start at index 1 and stop before the final point
    # because each point is compared with its neighbors
    for i in range(1, len(y_values) - 1):

        if (
            y_values[i] > y_values[i - 1]
            and y_values[i] > y_values[i + 1]
            and y_values[i] > 0
        ):
            peaks.append(
                (x_values[i], y_values[i])
            )

    # Sort peaks from strongest to weakest
    peaks.sort(
        key=lambda peak: peak[1],
        reverse=True
    )

    return peaks


# Create the comparison figure
plt.figure(figsize=(9, 5))


# Analyze each input file
for input_file in input_files:

    coordinate = []
    distribution = []

    # Open and read the .xvg file
    with input_file.open("r") as file:
        for line in file:

            line = line.strip()

            # Ignore empty lines
            if not line:
                continue

            # Ignore GROMACS / Grace metadata
            if line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            # Column 1 = distribution coordinate
            # Column 2 = distribution value
            coordinate.append(float(values[0]))
            distribution.append(float(values[1]))


    # Stop processing this file if no numerical data were found
    if not distribution:
        print(f"No numerical data found in {input_file}")
        continue


    # Find the global maximum
    max_value = max(distribution)

    max_index = distribution.index(max_value)

    peak_coordinate = coordinate[max_index]


    # Calculate a weighted mean coordinate
    total_weight = sum(distribution)

    if total_weight > 0:

        weighted_mean = sum(
            x * y
            for x, y in zip(coordinate, distribution)
        ) / total_weight

    else:
        weighted_mean = 0


    # Find local peaks
    local_peaks = find_local_peaks(
        coordinate,
        distribution
    )

    # Keep the four strongest local peaks
    top_peaks = local_peaks[:4]


    # Save summary information for CSV output
    summary_results.append(
        {
            "file": input_file.name,
            "peak_coordinate": peak_coordinate,
            "maximum_distribution_value": max_value,
            "weighted_mean_coordinate": weighted_mean,
            "number_of_local_peaks": len(local_peaks),
        }
    )


    # Print summary to terminal
    print(input_file.name)

    print(
        f"  Peak coordinate: "
        f"{peak_coordinate:.3f}"
    )

    print(
        f"  Maximum distribution value: "
        f"{max_value:.3f}"
    )

    print(
        f"  Weighted mean coordinate: "
        f"{weighted_mean:.3f}"
    )

    print(
        f"  Number of local peaks: "
        f"{len(local_peaks)}"
    )


    print("  Strongest local peaks:")

    if top_peaks:

        for peak_x, peak_y in top_peaks:

            print(
                f"    coordinate = {peak_x:.3f}, "
                f"value = {peak_y:.3f}"
            )

    else:
        print("    No positive local peaks detected.")

    print()


    # Add this distribution to the comparison plot
    plt.plot(
        coordinate,
        distribution,
        marker="o",
        linewidth=1.5,
        label=input_file.stem
    )


# Plot labels
plt.xlabel("Distribution coordinate")
plt.ylabel("Distribution value")

plt.title(
    "Headgroup Distribution Comparison"
)

plt.legend()

plt.tight_layout()


# Save figure
figure_output = Path(
    "figures/headgroup_distribution_comparison.png"
)

figure_output.parent.mkdir(
    parents=True,
    exist_ok=True
)

plt.savefig(
    figure_output,
    dpi=300
)


# Save numerical summary as CSV
csv_output = Path(
    "analysis/headgroup-analysis/"
    "headgroup_distribution_summary.csv"
)


with csv_output.open(
    "w",
    newline=""
) as csv_file:

    fieldnames = [
        "file",
        "peak_coordinate",
        "maximum_distribution_value",
        "weighted_mean_coordinate",
        "number_of_local_peaks",
    ]

    writer = csv.DictWriter(
        csv_file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(
        summary_results
    )


print(
    f"Figure saved to: "
    f"{figure_output}"
)

print(
    f"Summary saved to: "
    f"{csv_output}"
)


# Display the figure
plt.show()