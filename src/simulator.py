import random

def get_meter_readings():
    readings = []
    for i in range(1, 6):
        reading = {
            'meter_id': f'Meter {i}',
            'power': random.uniform(100, 500)  # Simulated power consumption in Watts
        }
        readings.append(reading)
    return readings
