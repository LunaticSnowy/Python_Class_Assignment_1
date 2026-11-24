import random
random.seed(256)

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from inc.sensorInterface import sensor_interface
from inc.sensorFile import save_sensor_data, load_sensor_data
from inc.sensorAnalysis import sensor_analysis
from inc.sensorVisualization import sensor_visualization


def input_sensor(
    prompt: str = "Choose IMU or ADC: "
) -> str:

    while True:
        choice = input(prompt).strip().upper()

        if choice in ("IMU", "ADC"):
            return choice

        print("Invalid input. Please try again.")


def input_float(
    prompt: str
) -> float:

    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("Invalid input. Please enter a number.")


def input_int(
    prompt: str
) -> int:

    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    # Choose between generating or loading data.
    print("\nSensor Application: ")
    print(" 1. Generate new sensor readings")
    print(" 2. Load readings from CSV")

    while True:
        choice = input("Choose an option: ").strip()

        if choice in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    # Option 1: Generate new readings.
    if choice == "1":
        chosenSensor = input_sensor("[ IMU ] or [ ADC ]: ")

        if chosenSensor == "IMU":
            lowerBound = input_float("Enter lowerbound: ")
            upperBound = input_float("Enter upperbound: ")
            alertBound = input_float("Enter alertbound: ")
            cycles     = input_int("Enter cycles: ")

        else:  # ADC
            lowerBound = input_int("Enter lowerbound: ")
            upperBound = input_int("Enter upperbound: ")
            alertBound = input_int("Enter alertbound: ")
            cycles     = input_int("Enter cycles: ")

        # Validate configuration.
        if lowerBound >= upperBound:
            print("Error: Lowerbound must be smaller than upperbound.")
            return

        if cycles <= 0:
            print("Error: Cycles must be greater than zero.")
            return

        userInput: dict[str, float | int] = {
            "lowerBound": lowerBound,
            "upperBound": upperBound,
            "alertBound": alertBound,
            "cycles"    : cycles
        }

        sensorData = sensor_interface(userInput, chosenSensor)

        # Save generated readings.
        filename = input("Enter filename to save (default: sensor_data.csv): ").strip()

        if not filename:
            filename = "sensor_data.csv"

        save_sensor_data(sensorData, filename)

    # Option 2: Load existing CSV data.
    else:
        filename = input("Enter CSV filename to load: ").strip()

        if not filename:
            print("Filename cannot be empty.")
            return

        try:
            sensorData = load_sensor_data(filename)

        except FileNotFoundError:
            print("Error: File not found.")
            return

        except (ValueError, TypeError) as error:
            print(f"Error loading CSV: {error}")
            return

        alertBound = input_float("Enter alertbound: ")

    # Analysis.
    print("\nSensor Analysis: ")
    sensor_analysis(sensorData, alertBound)

    # Visualization.
    print("\nSensor Visualization:")
    sensor_visualization(sensorData, alertBound)
    
    # Finish.
    print("The script has finished.")

if __name__ == "__main__":
    main()