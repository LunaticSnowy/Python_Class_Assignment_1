import numpy as np

def sensor_analysis(
    sensorData: dict[str, list[int | float]] | list[int | float], alertBound: float
    ) -> None:

    if isinstance(sensorData, dict):
        axes = sensorData
    elif isinstance(sensorData, list):
        axes = {"Sensor": sensorData}
    else:
        raise TypeError("Input must be a dictionary or list.")

    for axis, readings in axes.items():
        data = np.array(readings, dtype=float)

        if data.size == 0:
            print(f"\n    {axis}    ")
            print("No readings available.")
            continue

        numberOfReadings  = len(data)
        mean              = np.mean(data)
        minimum           = np.min(data)
        maximum           = np.max(data)
        standardDeviation = np.std(data)

        alertReadings = data[data > alertBound]
        alertCount    = len(alertReadings)

        print(f"\n========== {axis} ==========")

        print(f"Number of readings: {numberOfReadings}")
        print(f"Mean: {mean:.3f}")
        print(f"Minimum: {minimum:.3f}")
        print(f"Maximum: {maximum:.3f}")
        print(f"Standard deviation: {standardDeviation:.3f}")

        print(f"Readings above alert threshold: {alertCount}")
        print(f"Alert threshold: {alertBound}")

        print("Alert readings:", alertReadings.tolist())
