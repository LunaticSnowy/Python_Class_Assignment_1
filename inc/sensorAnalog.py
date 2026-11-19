"""
This will simulate a analog peripheral running through a ADC.
"""

from inc.helperRNG import generate_ADC_readings

def sensor_init(sensorInit: dict[str, int]) -> dict[str, int | str]:
    """
        Just imagine there's tons of very important initialisation logic happening in here.
    """

    sensorInstance: dict[str, int | str] = {
        "lowerBound" : sensorInit["lowerBound"],
        "upperBound" : sensorInit["upperBound"],
        "alertBound" : sensorInit["alertBound"],
        "cycles"     : sensorInit["cycles"],
        "sensorType" : "ADC"
    }
    return sensorInstance

def sensor_reading(sensorInstance: dict[str, int]) -> list[int]:
    sensorResult: list[int] = []

    rngConfig: dict[str, int] = {
        "lowerBound" : sensorInstance["lowerBound"],
        "upperBound" : sensorInstance["upperBound"],
    }

    for _ in range(sensorInstance["cycles"]):
        sensorResult.append(
            generate_ADC_readings(rngConfig)
        )

    return sensorResult