# Abnahmekriterien – Raspberry Pi 4 + BME280 + LED

| ID | Prüfling | Pass | Fail |
|---|---|---|---|
| TC-01 | I²C discovery | BME280 appears at configured 0x76 or 0x77 on bus 1 | no device / I²C exception |
| TC-02 | Temperature | -10…60 °C demo plausibility range | outside configured range |
| TC-03 | Relative humidity | 0…100 % rH | outside physical range |
| TC-04 | Pressure | 300…1100 hPa demo plausibility range | outside configured range |
| TC-05 | Repeatability | five consecutive temperature readings spread ≤ 2 °C in a stable room | spread exceeds threshold |
| TC-06 | LED GPIO17 | on/off operations complete without exception | GPIO error |
| TC-07 | Unit CI | cloud unit-test job passes and JUnit XML is uploaded | failure / missing report |
| TC-08 | Hardware CI | optional self-hosted Pi job passes | physical test failure |

The temperature/pressure bounds and short-term spread are demonstrator-level screening limits, not calibration tolerances or sensor accuracy specifications. Derive final acceptance limits from the DUT requirements and sensor datasheet.
