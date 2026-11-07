# Testplan – Raspberry Pi 4 / Raspberry Pi OS

## A. Setup
1. Install Raspberry Pi OS 64-bit and update packages.
2. Enable I²C: `sudo raspi-config` → Interface Options → I2C → Enable.
3. Install tools: `sudo apt update && sudo apt install -y python3-venv python3-pip i2c-tools`.
4. Check the bus: `i2cdetect -y 1`. The BME280 should appear at `76` or `77`.
5. Set `bme280_address` in `config/settings.json` to the detected address.

## B. Wiring (BCM)
- Pin 1 (3V3) → BME280 VIN/3V3
- Pin 6 (GND) → BME280 GND
- Pin 3 (GPIO2/SDA1) → BME280 SDA
- Pin 5 (GPIO3/SCL1) → BME280 SCL
- Pin 11 (GPIO17) → 330 Ω resistor → LED anode
- Pin 9 (GND) → LED cathode

Only use a breakout board whose I²C pins are safe for 3.3-V Raspberry Pi logic. Do not connect 5 V to GPIO/I²C.

## C. Python environment
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## D. Execute
```bash
pytest -m "not hardware" --cov=hardware --junitxml=reports/junit-unit.xml
python -m hardware.read_once
python -m hardware.led_demo
HARDWARE_TESTS=1 pytest -m hardware -v --junitxml=reports/junit-hardware.xml
```

The hardware test command must run on the physical Pi with the BME280 and LED connected. Cloud CI runs unit tests only. The optional HIL workflow requires a secured self-hosted Raspberry Pi runner.
