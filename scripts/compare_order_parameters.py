from pathlib import Path
import sys
import csv
import statistics
import matplotlib.pyplot as plt


# Require at least two files
if len(sys.argv) < 3:
    print(
        "Usage: python scripts/compare_order_parameters.py "
        "<file1> <file2> [file3 ...]"
    )
    sys.exit(1)


input_files = [Path(filename) for filename in sys.argv[1:]]

summary_results = []

plt.figure(figsize=(9, 5))


for input_file in input_files:

    segment = []
    order_parameter = []

    with input_file.open("r") as file:
        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            segment.append(int(float(values[0])))
            order_parameter.append(float(values[1]))

    if not order_parameter:
        print(f"No numerical data found in {input_file}")
        continue

    mean_order = statistics.mean(order_parameter)
    min_order = min(order_parameter)
    max_order = max(order_parameter)

    min_index = order_parameter.index(min_order)
    max_index = order_parameter.index(max_order)

    min_segment = segment[min_index]
    max_segment = segment[max_index]

    # Save summary values
    summary_results.append(
        {
            "file": input_file.name,
            "segments": len(order_parameter),
            "mean_S_CD": mean_order,
            "minimum_S_CD": min_order,
            "minimum_segment": min_segment,
            "maximum_S_CD": max_order,
            "maximum_segment": max_segment,
        }
    )

    # Print summary
    print(input_file.name)
    print(f"  Mean S_CD: {mean_order:.3f}")
    print(f"  Minimum S_CD: {min_order:.3f} at segment {min_segment}")
    print(f"  Maximum S_CD: {max_order:.3f} at segment {max_segment}")
    print()

    # Plot profile
    plt.plot(
        segment,
        order_parameter,
        marker="o",
        linewidth=1.5,
        label=input_file.stem
    )


# Plot formatting
plt.xlabel("Lipid-tail segment index")
plt.ylabel("Order parameter (S_CD)")
plt.title("Comparison of Lipid Order-Parameter Profiles")

plt.legend()
plt.tight_layout()


# Save figure
figure_output = Path("figures/order_parameter_comparison.png")

figure_output.parent.mkdir(
    parents=True,
    exist_ok=True
)

plt.savefig(
    figure_output,
    dpi=300
)


# Save CSV summary
csv_output = Path(
    "analysis/order-parameters/order_parameter_summary.csv"
)

with csv_output.open("w", newline="") as csv_file:

    fieldnames = [
        "file",
        "segments",
        "mean_S_CD",
        "minimum_S_CD",
        "minimum_segment",
        "maximum_S_CD",
        "maximum_segment",
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