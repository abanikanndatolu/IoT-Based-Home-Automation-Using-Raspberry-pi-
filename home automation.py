# home_automation.py
from flask import Flask, render_template
import RPi.GPIO as GPIO

# Flask setup
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
pins = {'Light': 17, 'Fan': 27}
for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

@app.route("/")
def index():
    return render_template("index.html", pins=pins)

@app.route("/<device>/<action>")
def control(device, action):
    pin = pins[device]
    GPIO.output(pin, GPIO.HIGH if action == "on" else GPIO.LOW)
    return f"{device} turned {action}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)