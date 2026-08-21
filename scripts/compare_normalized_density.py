from pathlib import Path
import sys
import matplotlib.pyplot as plt


if len(sys.argv) < 3:
    print(
        "Usage: python scripts/compare_normalized_density.py "
        "<file1> <file2> [file3 ...]"
    )
    sys.exit(1)


input_files = [Path(filename) for filename in sys.argv[1:]]


plt.figure(figsize=(9, 5))


for input_file in input_files:

    z_coordinate = []
    density = []

    with input_file.open("r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#") or line.startswith("@"):
                continue

            values = line.split()

            z_coordinate.append(float(values[0]))
            density.append(float(values[1]))


    if not density:
        print(f"No numerical data found in {input_file}")
        continue


    max_density = max(density)

    if max_density <= 0:
        print(
            f"Cannot normalize {input_file.name}: "
            "maximum value is zero."
        )
        continue


    normalized_density = [
        value / max_density
        for value in density
    ]


    peak_index = density.index(max_density)

    peak_z = z_coordinate[peak_index]


    print(input_file.name)
    print(f"  Original maximum: {max_density:.3f}")
    print(f"  Normalized maximum: 1.000")
    print(f"  Peak z-coordinate: {peak_z:.3f}")
    print()


    plt.plot(
        z_coordinate,
        normalized_density,
        linewidth=1.8,
        label=input_file.stem
    )


plt.xlabel("Z coordinate")
plt.ylabel("Normalized density")

plt.title(
    "Normalized Density Profiles Along the Bilayer Normal"
)

plt.ylim(0, 1.05)

plt.legend()

plt.tight_layout()


output_file = Path(
    "figures/normalized_density_comparison.png"
)

output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)

plt.savefig(
    output_file,
    dpi=300
)


print(f"Figure saved to: {output_file}")

plt.show()