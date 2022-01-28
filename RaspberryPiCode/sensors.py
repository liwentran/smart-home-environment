"""Kookye Sensors on the RaspberryPi

This module allows you to read data from the sensors and control them.

    Typical usage example:
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
    
    def __init__(self, pin):
        """Inits LED with pin"""
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT, initial=0)
        pass

    def on(self):
        """Turns on the light"""
        
        GPIO.output(self.pin, 1)
        pass

    def off(self):
        """Turns off the light"""

        GPIO.output(self.pin, 0)
        pass


    def blink_once(self):
        """LED blinks once """
        self.on()
        sleep(0.5)
        self.off()
        pass


class Touch:
    """A class used to represent the Kookye Touch Sensor
    
    Args:
        pin: The GPIO pin umber the touch sensor is connected to (use pinout to look up)

    Attributes:
        touch_state: A boolean indicating if the sensor is touched or not.
    """
    
    def __init__(self, pin):
        """Inits Touch with pin"""
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.pin = pin
        self.touch_state = self.get_state()
        pass
    
    def get_state(self):
        """Fetches the state of the touch sensor

        Returns:
            A boolean representing if the touch sensor is touched.
            1 for touched, and 0 for untouched.
        """
        touch_state = GPIO.input(self.pin)
        return touch_state

    def __str__(self):
        """String method that shows the current state of the sensor

        Returns: 
             The string representation of the state. For example:
             
             Touch Sensor State: Touched
        """
        s = "Touch Sensor State: "
        if (self.get_state() == 1):
            s += "Touched"
        else:
            s+= "Untouched"
        return s

class MockSensor:
    """A class used to represent a sensor

    Attributes:
        state: A random boolean representing the state of the sensor
        value: A random integer value representing a sensor value
    """

    state = True
    value = 0

    def get_state(self):
        """Generates a random state for the mock sensor
        
        Returns:
           A boolean value representing a true or false state
        """
        if (random.randint(0,9) > 5):
            self.state = False
        else:
            self.state = True
        return self.state

    def get_value(self):
        """Generates a random value between 0 and 10

        Returns:
            A random integer representing some data
        """
        self.value = random.randint(0,10)
        return self.value
