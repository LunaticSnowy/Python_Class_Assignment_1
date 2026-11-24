from inc.sensorIMU import sensor_init as imu_init
from inc.sensorIMU import sensor_reading as imu_reading

from inc.sensorAnalog import sensor_init as adc_init
from inc.sensorAnalog import sensor_reading as adc_reading

def sensor_interface(
    userInput: dict[str, float | int], chosenSensor: str
) -> dict[str, list[float]] | list[int]:

    sensorInitConfig: dict[str, float | int] = {
        "lowerBound": userInput["lowerBound"],
        "upperBound": userInput["upperBound"],
        "alertBound": userInput["alertBound"],
        "cycles"    : userInput["cycles"]
    }

    if chosenSensor == "IMU":
        sensor = imu_init(sensorInitConfig)
        result = imu_reading(sensor)

    elif chosenSensor == "ADC":
        sensor = adc_init(sensorInitConfig)
        result = adc_reading(sensor)

    else:
        raise ValueError(f"Unknown sensor: {chosenSensor}")

    #print(result)
    return result