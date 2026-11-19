"""
    This will simulate being a IMU.
"""

from inc.helperRNG import generate_IMU_readings

def sensor_init(sensorInitConfig: dict[str, float | int]) -> dict[str, float | int | str]:
    """
        Just imagine there's tons of very important initialisation logic happening in here.
    """
 
    sensorInstance: dict[str, float | int | str] = {
        "lowerBound" : sensorInitConfig["lowerBound"],
        "upperBound" : sensorInitConfig["upperBound"],
        "alertBound" : sensorInitConfig["alertBound"],
        "cycles"     : sensorInitConfig["cycles"],
        "sensorType" : "IMU"
    }

    return sensorInstance

def sensor_reading(sensorInstance: dict[str, float | int]) -> dict[str, list[float]]:
    sensorResult: dict[str, list[float]] = {
    "X" : [],
    "Y" : [],
    "Z" : []
    }

    rngConfig: dict[str, float] = {
        "lowerBound" : sensorInstance["lowerBound"],
        "upperBound" : sensorInstance["upperBound"],
    }

    for axis in sensorResult:
        for _ in range(sensorInstance["cycles"]):
            sensorResult[axis].append(
                generate_IMU_readings(rngConfig)
            )

    return sensorResult