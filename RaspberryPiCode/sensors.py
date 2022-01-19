import RPi.GPIO as GPIO
from time import sleep
import os
import random

# GPIO port init
def init():
    GPIO.setmode(GPIO.BCM)
    print('GPIO initialized')

# GPIO clean up
def cleanup():
    GPIO.cleanup()
    print('GPIO Cleaned up')

# LED light bulb
class LED:
    # LED init
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT, initial=0)
        pass

    # turn on LED
    def on(self):
        GPIO.output(self.pin, 1)
        pass

    # turn off LED
    def off(self):
        GPIO.output(self.pin, 0)
        pass

    # LED blinks once
    def blink_once(self):
        self.on()
        time.sleep(0.5)
        self.off()
        pass

# Kookye touch sensor
class touch:
    # tracks the state of the touch sensor
    touch_state = 0

    # touch sensor init
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        touch_state = self.get_state()
        pass

    # returns 1 if touched and 0 if not touched
    def get_state(self):
        touch_state = GPIO.input(self.pin)
        return touch_state

    # returns the state of touch sensor
    def __str__(self):
        s = "Touch Sensor State: "
        if (self.get_state() == 1):
            s += "Touched"
        else:
            s+= "Untouched"
        return s

# mock sensor 
class MockSensor:
    state  = True
    value = 0

    # returns true or false at random
    def get_state(self):
        if (random.randint(0,9) > 5):
            self.state = False
        else:
            self.state = True

        return self.state

    # returns an integer between 0 and 10
    def get_value(self):
        self.value = random.randint(0,10)
        return self.value
