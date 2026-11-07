"""Switch the status LED on for one second, then off."""
import json
from pathlib import Path
from time import sleep
from hardware.actuators import StatusLED

def main():
    cfg=json.loads(Path("config/settings.json").read_text(encoding="utf-8"))
    led=StatusLED(cfg["led_gpio_bcm"])
    try:
        led.on()
        sleep(1)
        led.off()
    finally:
        led.close()

if __name__=="__main__":
    main()
