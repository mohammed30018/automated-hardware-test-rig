"""GPIO17 status LED adapter (BCM numbering)."""
class StatusLED:
    def __init__(self, pin: int = 17):
        if not isinstance(pin, int) or not 0 <= pin <= 27:
            raise ValueError("Use a valid Raspberry Pi BCM GPIO number.")
        try:
            from gpiozero import LED
        except ImportError as exc:
            raise RuntimeError("gpiozero is missing; install requirements.txt.") from exc
        self._led = LED(pin)

    def on(self) -> None:
        self._led.on()

    def off(self) -> None:
        self._led.off()

    def close(self) -> None:
        self._led.close()
