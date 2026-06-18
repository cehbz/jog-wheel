# jog-wheel

A DIY weighted jog/shuttle wheel for video editing — a heavy, low-friction wheel for scrubbing an NLE timeline (Premiere / Final Cut / Resolve), with frame-stepping left to the keyboard.

Status: design phase, parts on order. Not built yet.

## Direction

- **Feel:** a moderately heavy wheel that coasts, with *adjustable* drag — the inertia is fixed at build time but a tunable eddy-current brake (a conductive disc near an adjustable magnet) sweeps from near-frictionless coast to quick-settle without touching the wheel.
- **Wheel:** a ~6 cm knurled cylinder, vertical axis. Mass from a thick rim, not a solid billet. Either a detent-free ball-bearing optical encoder (LPD3806-600 class) that doubles as the spindle, or a dedicated two-bearing spindle with a magnetic encoder if the cheap encoder's bearing drag kills the coast.
- **Brain:** MCU (TBD) reading the quadrature in hardware, presenting as USB HID. Firmware maps angular *velocity* to scrub speed via ramped J-K-L with a sub-threshold deadband, so the coast's exponential tail never drifts the playhead. Rate control, not position control — a free-coasting wheel can't couple position to the timeline.

Open tasks in `TODO.md`.

## Relationship to spacekit

This project started the investigation into mouse tilt-wheel → macOS Space switching. That work outgrew the knob and became its own toolkit, [spacekit](https://github.com/cehbz/spacekit) (a general scroll-tilt daemon, not knob-specific). The jog wheel is the hardware half that never got built; the two are independent now.
