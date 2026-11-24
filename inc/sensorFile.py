import csv

def save_sensor_data(
    sensorData: dict[str, list[float]] | list[int | float],
    filename: str
) -> None:

    # Determine the CSV columns.
    if isinstance(sensorData, dict):
        headers = ["Sample number"] + list(sensorData.keys())

        # Ensure all axes contain the same number of readings.
        lengths = {len(readings) for readings in sensorData.values()}
        if len(lengths) > 1:
            raise ValueError("All sensor axes must have equal lengths.")

        numberOfReadings = next(iter(lengths), 0)

    elif isinstance(sensorData, list):
        headers = ["Sample number", "Reading"]
        numberOfReadings = len(sensorData)

    else:
        raise TypeError("Input must be a dictionary or list.")

    # Write the data to CSV.
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for i in range(numberOfReadings):
            if isinstance(sensorData, dict):
                row = [i + 1] + [
                    sensorData[axis][i] for axis in sensorData
                ]
            else:
                row = [i + 1, sensorData[i]]

            writer.writerow(row)

    print(f"Sensor data saved to {filename}.")


def load_sensor_data(
    filename: str
) -> dict[str, list[float]] | list[float]:

    sensorData = {}

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None or "Sample number" not in reader.fieldnames:
            raise ValueError("Invalid CSV file: missing Sample number column.")

        # Determine whether this is ADC or IMU data.
        if "Reading" in reader.fieldnames:
            sensorType = "ADC"
            sensorData = {"Reading": []}
        else:
            sensorType = "IMU"
            axes = [
                column for column in reader.fieldnames
                if column != "Sample number"
            ]

            if not axes:
                raise ValueError("CSV file contains no sensor readings.")

            sensorData = {axis: [] for axis in axes}

        for row in reader:
            if sensorType == "ADC":
                sensorData["Reading"].append(float(row["Reading"]))
            else:
                for axis in sensorData:
                    sensorData[axis].append(float(row[axis]))

    # Return ADC as a list, IMU as a dictionary.
    if sensorType == "ADC":
        return sensorData["Reading"]

    return sensorData
