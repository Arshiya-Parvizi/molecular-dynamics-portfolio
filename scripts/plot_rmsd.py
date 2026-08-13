from pathlib import Path
import sys
import statistics
import matplotlib.pyplot as plt


# Check that an input file was provided
if len(sys.argv) < 2:
    print("Usage: python scripts/plot_rmsd.py <rmsd_file>")
    sys.exit(1)


# Input and output paths
input_file = Path(sys.argv[1])
output_file = Path("figures") / f"{input_file.stem}.png"


# Store data
time = []
rmsd = []


# Read the GROMACS .xvg file
with input_file.open("r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        # Skip GROMACS/Grace metadata if present
        if line.startswith("#") or line.startswith("@"):
            continue

        values = line.split()

        time.append(float(values[0]))
        rmsd.append(float(values[1]))


# Check that numerical data were found
if not rmsd:
    print("No numerical RMSD data found.")
    sys.exit(1)


# Calculate summary statistics
mean_rmsd = statistics.mean(rmsd)
min_rmsd = min(rmsd)
max_rmsd = max(rmsd)
std_rmsd = statistics.stdev(rmsd)
# Analyze the final 20% of the trajectory separately
late_start_index = int(len(rmsd) * 0.8)

late_time = time[late_start_index:]
late_rmsd = rmsd[late_start_index:]

late_mean_rmsd = statistics.mean(late_rmsd)
late_std_rmsd = statistics.stdev(late_rmsd)

# Print results
print(f"Data points: {len(rmsd)}")
print(f"Mean RMSD: {mean_rmsd:.3f} nm")
print(f"Minimum RMSD: {min_rmsd:.3f} nm")
print(f"Maximum RMSD: {max_rmsd:.3f} nm")
print(f"Standard deviation: {std_rmsd:.3f} nm")
print()
print("Final 20% of trajectory:")
print(f"Mean RMSD: {late_mean_rmsd:.3f} nm")
print(f"Standard deviation: {late_std_rmsd:.3f} nm")

# Create the plot
plt.figure(figsize=(8, 5))

plt.plot(time, rmsd, linewidth=1)
plt.axvspan(
    late_time[0],
    late_time[-1],
    alpha=0.15,
    label="Final 20%"
)
# Add the mean RMSD as a reference line
plt.axhline(
    y=mean_rmsd,
    linestyle="--",
    linewidth=1,
    label=f"Mean RMSD = {mean_rmsd:.3f} nm"
)

plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title(f"RMSD: {input_file.stem}")

plt.legend()
plt.tight_layout()


# Make sure the figures directory exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Save figure
plt.savefig(output_file, dpi=300)

# Display figure
plt.show()