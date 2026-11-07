"""BME280 driver adapter for Raspberry Pi 4 / Raspberry Pi OS."""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class EnvironmentReading:
    temperature_c: float
    humidity_percent: float
    pressure_hpa: float

    def validate_finite(self) -> None:
        values = (self.temperature_c, self.humidity_percent, self.pressure_hpa)
        if not all(math.isfinite(float(v)) for v in values):
            raise ValueError("Sensor returned a non-finite measurement.")

class BME280Sensor:
    """I2C BME280 adapter. Common breakout addresses are 0x76 and 0x77."""
    def __init__(self, address: int = 0x76):
        if address not in (0x76, 0x77):
            raise ValueError("BME280 I2C address must be 0x76 or 0x77.")
        try:
            import board
            import busio
            import adafruit_bme280.basic
        except ImportError as exc:
            raise RuntimeError(
                "Missing BME280 dependencies. Install requirements.txt on Raspberry Pi OS."
            ) from exc
        self._i2c = busio.I2C(board.SCL, board.SDA)
        self._device = adafruit_bme280.basic.Adafruit_BME280_I2C(
            self._i2c, address=address
        )

    def read(self) -> EnvironmentReading:
        reading = EnvironmentReading(
            temperature_c=float(self._device.temperature),
            humidity_percent=float(self._device.relative_humidity),
            pressure_hpa=float(self._device.pressure),
        )
        reading.validate_finite()
        return reading

    def close(self) -> None:
        deinit = getattr(self._i2c, "deinit", None)
        if callable(deinit):
            deinit()
