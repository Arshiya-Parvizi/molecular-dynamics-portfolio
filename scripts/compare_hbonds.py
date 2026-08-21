from pathlib import Path
import sys
import csv
import statistics
import matplotlib.pyplot as plt


# Require at least two hydrogen-bond files
if len(sys.argv) < 3:
    print(
        "Usage: python scripts/compare_hbonds.py "
        "<file1> <file2> [file3 ...]"
    )
    sys.exit(1)


input_files = [Path(filename) for filename in sys.argv[1:]]

summary_results = []

labels = []
occupancies = []


for input_file in input_files:

    hbond_count = []

    # Read numerical data
    with input_file.open("r") as file:
        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            # Second column = hydrogen-bond count
            hbond_count.append(float(values[1]))

    if not hbond_count:
        print(f"No numerical data found in {input_file}")
        continue

    mean_hbonds = statistics.mean(hbond_count)
    max_hbonds = max(hbond_count)

    frames_with_hbond = sum(
        value > 0 for value in hbond_count
    )

    occupancy = (
        frames_with_hbond / len(hbond_count)
    ) * 100

    # Store for CSV
    summary_results.append(
        {
            "file": input_file.name,
            "data_points": len(hbond_count),
            "mean_hbonds_per_frame": mean_hbonds,
            "max_hbonds_per_frame": max_hbonds,
            "frames_with_hbond": frames_with_hbond,
            "occupancy_percent": occupancy,
        }
    )

    # Store for graph
    labels.append(input_file.stem)
    occupancies.append(occupancy)

    # Print result
    print(input_file.name)
    print(f"  Mean H-bonds/frame: {mean_hbonds:.3f}")
    print(f"  Maximum H-bonds/frame: {max_hbonds:.0f}")
    print(f"  Occupancy: {occupancy:.2f}%")
    print()


# Create occupancy comparison plot
plt.figure(figsize=(9, 5))

bars = plt.bar(labels, occupancies)

# Add occupancy values above each bar
for bar, occupancy in zip(bars, occupancies):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{occupancy:.1f}%",
        ha="center",
        va="bottom"
    )

plt.ylabel("Hydrogen-bond occupancy (%)")
plt.xlabel("Atom selection")
plt.title("Selected Hydrogen-Bond Interaction Occupancies")

plt.ylim(0, 110)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()


# Save figure
figure_output = Path(
    "figures/hbond_occupancy_comparison.png"
)

figure_output.parent.mkdir(
    parents=True,
    exist_ok=True
)

plt.savefig(
    figure_output,
    dpi=300
)


# Save numerical summary
csv_output = Path(
    "analysis/hydrogen-bonds/hbond_summary.csv"
)

with csv_output.open("w", newline="") as csv_file:

    fieldnames = [
        "file",
        "data_points",
        "mean_hbonds_per_frame",
        "max_hbonds_per_frame",
        "frames_with_hbond",
        "occupancy_percent",
    ]

    writer = csv.DictWriter(
        csv_file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(summary_results)


print(f"Figure saved to: {figure_output}")
print(f"Summary saved to: {csv_output}")

plt.show()