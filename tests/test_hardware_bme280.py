import os, json, pytest
from pathlib import Path
from hardware.sensors import BME280Sensor

pytestmark=pytest.mark.hardware

def test_bme280_live_measurements():
    if os.getenv("HARDWARE_TESTS") != "1":
        pytest.skip("Enable only on the Raspberry Pi with BME280 connected.")
    cfg=json.loads(Path("config/settings.json").read_text(encoding="utf-8"))
    sensor=BME280Sensor(int(cfg["bme280_address"],16))
    try:
        readings=[sensor.read() for _ in range(cfg["sampling"]["samples"])]
        lim=cfg["sensor_limits"]
        for r in readings:
            assert lim["temperature_c"]["min"] <= r.temperature_c <= lim["temperature_c"]["max"]
            assert lim["humidity_percent"]["min"] <= r.humidity_percent <= lim["humidity_percent"]["max"]
            assert lim["pressure_hpa"]["min"] <= r.pressure_hpa <= lim["pressure_hpa"]["max"]
        temps=[r.temperature_c for r in readings]
        assert max(temps)-min(temps) <= cfg["sampling"]["temperature_max_spread_c"]
    finally:
        sensor.close()
