import os, pytest
from hardware.actuators import StatusLED

pytestmark=pytest.mark.hardware

def test_gpio17_led_switches_on_and_off():
    if os.getenv("HARDWARE_TESTS") != "1":
        pytest.skip("Enable only on Raspberry Pi with LED/resistor wired to BCM GPIO17.")
    led=StatusLED(17)
    try:
        led.on()
        led.off()
    finally:
        led.close()
