from pathlib import Path
import sys
import csv
import matplotlib.pyplot as plt


# Require at least two files
if len(sys.argv) < 3:
    print(
        "Usage: python scripts/compare_density_profiles.py "
        "<file1> <file2> [file3 ...]"
    )
    sys.exit(1)


input_files = [Path(filename) for filename in sys.argv[1:]]

summary_results = []


def find_local_peaks(x_values, y_values):
    """
    Detect simple local maxima.

    A point is considered a local peak when its value is larger
    than both neighboring points and greater than zero.
    """

    peaks = []

    for i in range(1, len(y_values) - 1):

        if (
            y_values[i] > y_values[i - 1]
            and y_values[i] > y_values[i + 1]
            and y_values[i] > 0
        ):
            peaks.append(
                (x_values[i], y_values[i])
            )

    # Strongest peaks first
    peaks.sort(
        key=lambda peak: peak[1],
        reverse=True
    )

    return peaks


plt.figure(figsize=(9, 5))


for input_file in input_files:

    z_coordinate = []
    density_value = []

    # Read .xvg data
    with input_file.open("r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            # Ignore GROMACS / Grace metadata
            if line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            z_coordinate.append(
                float(values[0])
            )

            density_value.append(
                float(values[1])
            )


    if not density_value:
        print(
            f"No numerical data found in {input_file}"
        )
        continue


    # Global maximum
    max_density = max(density_value)

    max_index = density_value.index(
        max_density
    )

    peak_z = z_coordinate[max_index]


    # Weighted mean
    total_density = sum(density_value)

    if total_density > 0:

        weighted_mean_z = sum(
            z * density
            for z, density
            in zip(z_coordinate, density_value)
        ) / total_density

    else:
        weighted_mean_z = 0


    # Detect local peaks
    local_peaks = find_local_peaks(
        z_coordinate,
        density_value
    )

    top_peaks = local_peaks[:4]


    # Store summary
    summary_results.append(
        {
            "file": input_file.name,
            "peak_z_coordinate": peak_z,
            "maximum_density_value": max_density,
            "weighted_mean_z_coordinate": weighted_mean_z,
            "number_of_local_peaks": len(local_peaks),
        }
    )


    # Print results
    print(input_file.name)

    print(
        f"  Peak z-coordinate: "
        f"{peak_z:.3f}"
    )

    print(
        f"  Maximum density value: "
        f"{max_density:.3f}"
    )

    print(
        f"  Weighted mean z-coordinate: "
        f"{weighted_mean_z:.3f}"
    )

    print(
        f"  Number of local peaks: "
        f"{len(local_peaks)}"
    )

    print(
        "  Strongest local peaks:"
    )


    if top_peaks:

        for peak_x, peak_y in top_peaks:

            print(
                f"    z = {peak_x:.3f}, "
                f"value = {peak_y:.3f}"
            )

    else:

        print(
            "    No positive local peaks detected."
        )


    print()


    # Plot
    plt.plot(
        z_coordinate,
        density_value,
        linewidth=1.5,
        label=input_file.stem
    )


plt.xlabel("Z coordinate")
plt.ylabel("Density value")

plt.title(
    "Density Profiles Along the Bilayer Normal"
)

plt.legend()

plt.tight_layout()


# Save figure
figure_output = Path(
    "figures/density_profile_comparison.png"
)

figure_output.parent.mkdir(
    parents=True,
    exist_ok=True
)

plt.savefig(
    figure_output,
    dpi=300
)


# Save CSV
csv_output = Path(
    "analysis/density-profiles/"
    "density_profile_summary.csv"
)

with csv_output.open(
    "w",
    newline=""
) as csv_file:

    fieldnames = [
        "file",
        "peak_z_coordinate",
        "maximum_density_value",
        "weighted_mean_z_coordinate",
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
    f"Figure saved to: {figure_output}"
)

print(
    f"Summary saved to: {csv_output}"
)


plt.show()