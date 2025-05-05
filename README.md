# Automatic Laptop Charger Control using Arduino and Python

This project automates a laptop charger using an Arduino board and Python. It monitors the laptop battery level and intelligently switches the charger on or off using a relay, helping extend battery life and prevent overcharging.

---

## Features

- **Battery Monitoring:** Uses Python's `psutil` to monitor battery percentage and charging status.
- **Arduino Relay Control:** Automatically turns on the charger when battery is below 25% and turns it off at 100%.
- **Status Indicator:** An LED connected to Arduino pin indicates charger status.
- **Safety Feature:** Waits for disconnection if battery is full and charger is still plugged in.

---

## Hardware Requirements

- Arduino Uno (or compatible)
- Relay module
- LED
- USB cable for Arduino
- Laptop running Windows

---

## Software Requirements

- Python 3.x
- [pyFirmata](https://pypi.org/project/pyfirmata/)
- [psutil](https://pypi.org/project/psutil/)
- Arduino IDE (for driver and initial board setup)

---

## Circuit Diagram

- Relay connected to digital pin **12**
- LED connected to digital pin **10** via a resistor
- Arduino connected to laptop via USB

---

## Installation

1. **Connect Arduino to your laptop.**
2. **Install Python libraries:**

```bash
pip install pyfirmata psutil
