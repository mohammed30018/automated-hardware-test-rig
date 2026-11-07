import sys
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from hardware.actuators import StatusLED

def test_led_on_off_close_without_physical_gpio(monkeypatch):
    fake=Mock()
    class FakeLED:
        def __new__(cls,pin):
            assert pin == 17
            return fake
    monkeypatch.setitem(sys.modules,"gpiozero",SimpleNamespace(LED=FakeLED))
    led=StatusLED(17)
    led.on(); led.off(); led.close()
    fake.on.assert_called_once()
    fake.off.assert_called_once()
    fake.close.assert_called_once()

def test_led_rejects_invalid_pin():
    with pytest.raises(ValueError):
        StatusLED(99)
