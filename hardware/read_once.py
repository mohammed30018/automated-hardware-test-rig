"""Read one BME280 sample using project configuration."""
import json
from pathlib import Path
from hardware.sensors import BME280Sensor

def main():
    cfg=json.loads(Path("config/settings.json").read_text(encoding="utf-8"))
    sensor=BME280Sensor(int(cfg["bme280_address"],16))
    try:
        r=sensor.read()
        print(f"Temperature: {r.temperature_c:.2f} °C")
        print(f"Humidity:    {r.humidity_percent:.2f} %")
        print(f"Pressure:    {r.pressure_hpa:.2f} hPa")
    finally:
        sensor.close()

if __name__=="__main__":
    main()
