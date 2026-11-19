import random
random.seed(256)

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from inc.sensorInterface import sensor_interface

def input_sensor(prompt: str) -> str:
    print("What sensor would you like to use?")

    while True:
        choice: str = input(prompt).strip().upper()

        if choice in ("IMU", "ADC"):
            return choice

        else:
            print("Invalid input. Please try again.")

def input_float(prompt: str) -> float:
    while True:
        try:
            value: float = float(input(prompt))
            return value

        except ValueError:
            print("Invalid input. Please try again.")

def input_int(prompt: str) -> float:
    while True:
        try:
            value: int = int(input(prompt))
            return value

        except ValueError:
            print("Invalid input. Please try again.")

def main():
    chosenSensor = input_sensor("[ IMU ] or [ ADC ]: ")

    if chosenSensor == "IMU":
        lowerBound   = input_float("Enter lowerbound: ")
        upperBound   = input_float("Enter upperbound: ")
        alertBound   = input_float("Enter alertbound: ")
        cycles       = input_int("Enter cycles: ")

    elif chosenSensor == "ADC":
        lowerBound = input_int("Enter lowerbound: ")
        upperBound = input_int("Enter upperbound: ")
        alertBound = input_int("Enter alertbound: ")
        cycles     = input_int("Enter cycles: ")

    else:
        print("This shouldn't be possible")
        return

    userInput: dict[str, float | int] = {
        "lowerBound" : lowerBound,
        "upperBound" : upperBound,
        "alertBound" : alertBound,
        "cycles"     : cycles
    }

    sensor_interface(userInput, chosenSensor)

if __name__ == "__main__":
    main()