from pathlib import Path
import sys
import statistics
import matplotlib.pyplot as plt


# Check that an input file was provided
if len(sys.argv) < 2:
    print("Usage: python scripts/plot_order_parameter.py <order_parameter_file>")
    sys.exit(1)


input_file = Path(sys.argv[1])
output_file = Path("figures") / f"{input_file.stem}.png"


segment = []
order_parameter = []


# Read GROMACS .xvg data
with input_file.open("r") as file:
    for line in file:

        line = line.strip()

        if not line:
            continue

        # Skip GROMACS/Grace metadata if present
        if line.startswith("#") or line.startswith("@"):
            continue

        values = line.split()

        segment.append(int(float(values[0])))
        order_parameter.append(float(values[1]))


if not order_parameter:
    print("No numerical order-parameter data found.")
    sys.exit(1)


# Calculate descriptive statistics
mean_order = statistics.mean(order_parameter)
min_order = min(order_parameter)
max_order = max(order_parameter)

min_index = order_parameter.index(min_order)
max_index = order_parameter.index(max_order)

min_segment = segment[min_index]
max_segment = segment[max_index]


print(f"Number of segments: {len(order_parameter)}")
print(f"Mean S_CD: {mean_order:.3f}")
print(f"Minimum S_CD: {min_order:.3f} at segment {min_segment}")
print(f"Maximum S_CD: {max_order:.3f} at segment {max_segment}")


# Create plot
plt.figure(figsize=(8, 5))

plt.plot(
    segment,
    order_parameter,
    marker="o",
    linewidth=1.5
)

# Mean reference line
plt.axhline(
    y=mean_order,
    linestyle="--",
    linewidth=1,
    label=f"Mean S_CD = {mean_order:.3f}"
)

plt.xlabel("Lipid-tail segment index")
plt.ylabel("Order parameter (S_CD)")
plt.title(f"Lipid Order Parameter: {input_file.stem}")

plt.xticks(segment)

plt.legend()
plt.tight_layout()


# Save figure
output_file.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(output_file, dpi=300)

plt.show()