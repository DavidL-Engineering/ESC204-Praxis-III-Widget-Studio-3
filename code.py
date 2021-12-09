### Written by David L. for ESC204 - Praxis III in the Division of Engineering Science at the University of Toronto
import board
import digitalio
import time
import adafruit_hcsr04

# Configure the internal GPIO connected to the LED as a digital output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Board constants
TRIGGER_PIN = board.GP17
ECHO_PIN = board.GP16

THRESHOLD_HEIGHT = 0

sonar = adafruit_hcsr04.HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN)

while True:

    plant_height = sonar.distance

    if plant_height > THRESHOLD_HEIGHT:
        print("Plants ready to harvest!")
        led.value = True

    time.sleep(300)