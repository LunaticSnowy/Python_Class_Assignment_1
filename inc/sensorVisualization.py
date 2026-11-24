import matplotlib.pyplot as plt

def sensor_visualization(
    sensorData: dict[str, list[int | float]] | list[int | float], alertBound: float
) -> None:

    if isinstance(sensorData, dict):
        axes = sensorData
    elif isinstance(sensorData, list):
        axes = {"Sensor": sensorData}
    else:
        raise TypeError("Input must be a dictionary or list.")

    for axis, readings in axes.items():
        if not readings:
            print(f"No readings available for {axis}.")
            continue

        sampleNumbers = range(1, len(readings) + 1)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Line plot
        ax1.plot(
            sampleNumbers,
            readings,
            marker="o",
            label="Sensor readings"
        )

        ax1.axhline(
            y=alertBound,
            color="red",
            linestyle="--",
            label=f"Alert threshold ({alertBound})"
        )

        ax1.set_title(f"{axis} | Sensor Readings")
        ax1.set_xlabel("Sample number")
        ax1.set_ylabel("Reading")
        ax1.grid(True)
        ax1.legend()

        # Histogram
        ax2.hist(
            readings,
            bins="auto",
            edgecolor="black",
            label="Reading distribution"
        )

        ax2.set_title(f"{axis} | Reading Distribution")
        ax2.set_xlabel("Sensor reading")
        ax2.set_ylabel("Frequency")
        ax2.grid(True)
        ax2.legend()

        # Improves layout and display
        fig.suptitle(f"Sensor Visualization: {axis}")
        fig.tight_layout()
        plt.show()
