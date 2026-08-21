from pathlib import Path
import sys
import statistics
import matplotlib.pyplot as plt


# Check that an input file was provided
if len(sys.argv) < 2:
    print("Usage: python scripts/plot_hbonds.py <hbond_file>")
    sys.exit(1)


input_file = Path(sys.argv[1])
output_file = Path("figures") / f"{input_file.stem}.png"


time_ns = []
hbond_count = []
third_series = []


# Read GROMACS .xvg data
with input_file.open("r") as file:
    for line in file:

        line = line.strip()

        if not line:
            continue

        # Skip metadata if present
        if line.startswith("#") or line.startswith("@"):
            continue

        values = line.split()

        # This file contains at least three numerical columns
        time_ps = float(values[0])
        hbonds = float(values[1])
        extra_value = float(values[2])

        # Convert picoseconds to nanoseconds
        time_ns.append(time_ps / 1000)

        hbond_count.append(hbonds)
        third_series.append(extra_value)


if not hbond_count:
    print("No numerical hydrogen-bond data found.")
    sys.exit(1)


# Descriptive statistics
mean_hbonds = statistics.mean(hbond_count)
max_hbonds = max(hbond_count)

# Frames containing at least one hydrogen bond
frames_with_hbond = sum(value > 0 for value in hbond_count)

occupancy = (frames_with_hbond / len(hbond_count)) * 100


print(f"Data points: {len(hbond_count)}")
print(f"Mean hydrogen bonds per frame: {mean_hbonds:.3f}")
print(f"Maximum hydrogen bonds in a frame: {max_hbonds:.0f}")
print(f"Frames with at least one hydrogen bond: {frames_with_hbond}")
print(f"Hydrogen-bond occupancy: {occupancy:.2f} %")


# Plot hydrogen-bond count over time
plt.figure(figsize=(9, 5))

plt.plot(
    time_ns,
    hbond_count,
    linewidth=1
)

plt.xlabel("Time (ns)")
plt.ylabel("Number of hydrogen bonds")
plt.title(f"Hydrogen-Bond Analysis: {input_file.stem}")

plt.tight_layout()


# Save figure
output_file.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_file, dpi=300)

plt.show()