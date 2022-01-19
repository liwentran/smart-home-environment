"""Kookye Sensors on the RaspberryPi

This module allows you to read data from the sensors and control them.

Example:
     Call sensors.init() to set the pi to accept pins
     Create the sensor and initialize with the pin number
         mock_sensor = sensors.MockSensor()
     Get the an output with get_state() or get_value()
         mock_sensor.get_state()
"""

import RPi.GPIO as GPIO
from time import sleep
import os
import random


def init():
    """Initializes the RaspberryPI for the sensors

    Sets the board mode to GPIO.BCM
    """
    GPIO.setmode(GPIO.BCM)
    print('GPIO initialized')

def cleanup():
    """Cleans up the RaspberryPI
    
    Calls GPIO.cleanup()
    """
    GPIO.cleanup()
    print('GPIO Cleaned up')


class LED:
    """A class used to represent an LED light
    
    Args:
        pin: The GPIO pin number the LED is connected to (use pinout to look up)

    Attributes:
        pin: An integer that stores pin number
    
    """
    
    # LED init
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT, initial=0)
        pass

    def on(self):
        """Turns on the light
        """
        
        GPIO.output(self.pin, 1)
        pass

    def off(self):
        """Turns off the light
        """

        GPIO.output(self.pin, 0)
        pass


    def blink_once(self):
        """LED blinks once
        """
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
