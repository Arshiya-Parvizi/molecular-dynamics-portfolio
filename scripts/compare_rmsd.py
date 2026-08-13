from pathlib import Path
import sys
import csv
import statistics
import matplotlib.pyplot as plt


# Require at least two RMSD files
if len(sys.argv) < 3:
    print("Usage: python scripts/compare_rmsd.py <file1> <file2> [file3 ...]")
    sys.exit(1)


input_files = [Path(filename) for filename in sys.argv[1:]]

plt.figure(figsize=(9, 5))
summary_results = []


for input_file in input_files:

    time = []
    rmsd = []

    # Read numerical data
    with input_file.open("r") as file:
        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            time.append(float(values[0]))
            rmsd.append(float(values[1]))

    if not rmsd:
        print(f"No numerical data found in {input_file}")
        continue


    # Final 20% statistics
    late_start_index = int(len(rmsd) * 0.8)
    late_rmsd = rmsd[late_start_index:]

    late_mean = statistics.mean(late_rmsd)
    late_std = statistics.stdev(late_rmsd)
    summary_results.append(
    {
        "file": input_file.name,
        "final_20_percent_mean_rmsd_nm": late_mean,
        "final_20_percent_std_rmsd_nm": late_std,
    }
)

    # Print summary
    print(input_file.name)
    print(f"  Final 20% mean RMSD: {late_mean:.3f} nm")
    print(f"  Final 20% standard deviation: {late_std:.3f} nm")
    print()


    # Plot trajectory
    plt.plot(
        time,
        rmsd,
        linewidth=1,
        label=input_file.stem
    )


plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("Comparison of RMSD Trajectories")

plt.legend()
plt.tight_layout()


# Save comparison figure
output_file = Path("figures/rmsd_comparison.png")

output_file.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_file, dpi=300)
# Save numerical summary as CSV
csv_output = Path("analysis/rmsd/rmsd_summary.csv")

with csv_output.open("w", newline="") as csv_file:
    fieldnames = [
        "file",
        "final_20_percent_mean_rmsd_nm",
        "final_20_percent_std_rmsd_nm",
    ]

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(summary_results)

print(f"Summary saved to: {csv_output}")
plt.show()