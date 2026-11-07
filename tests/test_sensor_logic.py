import math
import pytest
from hardware.sensors import EnvironmentReading

def test_environment_reading_values():
    r=EnvironmentReading(22.5,45.0,1013.2)
    assert r.temperature_c == 22.5
    assert r.humidity_percent == 45.0
    assert r.pressure_hpa == 1013.2

@pytest.mark.parametrize("reading",[
    EnvironmentReading(20.0,50.0,1000.0),
    EnvironmentReading(-5.0,0.0,300.0),
    EnvironmentReading(59.9,100.0,1100.0),
])
def test_finite_measurements_pass(reading):
    reading.validate_finite()

def test_non_finite_measurement_fails():
    with pytest.raises(ValueError):
        EnvironmentReading(float("nan"),50.0,1000.0).validate_finite()

def test_demo_acceptance_ranges():
    r=EnvironmentReading(23.0,40.0,1012.0)
    assert -10 <= r.temperature_c <= 60
    assert 0 <= r.humidity_percent <= 100
    assert 300 <= r.pressure_hpa <= 1100
