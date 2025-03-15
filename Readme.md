# IoT-Based Home Automation

## Description
Control home appliances via a web interface using Raspberry Pi GPIO.

## Requirements
- Raspberry Pi 3B
- Relays
- Flask (`pip install flask`)
- Jumper wires
- Breadboard

## How to Run
1. Connect the relays to GPIO pins (17 for light, 27 for fan).
2. Start the server: `python3 home_automation.py`.
3. Open a browser and visit `http://<Raspberry Pi IP>:5000`.

## License
MIT