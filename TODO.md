# TODO — jog/shuttle wheel

## Videyt USB knob

- Restore bottom knob: try Videyt Windows app on native Windows hardware (see KB for full context).

## DIY jog wheel

- Test encoder + aluminum knob when parts arrive — evaluate coast feel and bearing drag.
- If coast disappoints: dedicated two-bearing spindle + MT6701 magnetic encoder.
- Choose MCU (likely ESP32 family).
- Firmware: hardware quadrature decode, velocity-thresholded J-K-L with ramp, sub-threshold deadband.
- Nice-to-have: adjustable eddy-current brake (aluminum disc + magnet on thumbscrew bracket). Add if easy, drop if not.
