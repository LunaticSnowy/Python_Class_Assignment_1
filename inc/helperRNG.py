import random

def generate_IMU_readings(
    rngConfig: dict[str, float]
) -> float:

    result: float = random.uniform(
        rngConfig["lowerBound"],
        rngConfig["upperBound"])
    return result

def generate_ADC_readings(
    rngConfig: dict[str, int]
) -> int:
    
    result: int = random.randint(
        rngConfig["lowerBound"],
        rngConfig["upperBound"])
    return result