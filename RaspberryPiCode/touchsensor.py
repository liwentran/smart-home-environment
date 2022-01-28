import RPi.GPIO as GPIO
import time
import os

# pin values
sensor = 26
light = 18

# tracks state of touch sensor
touch_state = 0;

# GPIO port init
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(light, GPIO.OUT, initial=0)
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    pass

# read touch sensor
def read_touchsensor():
    touch_state = GPIO.input(sensor)
    if(touch_state == True):
        print("Touch sensor: touched")
        light_on()
    else:
        print("Touch sensor: not touched")
        light_off()
    pass

# turn off LED
def light_on():
    GPIO.output(light,1)
    pass

# turn on LED
def light_off():
    GPIO.output(light,0)
    pass

# flash on and off LED
def light_flash():
    light_on()
    time.sleep(0.5)
    light_off()
    time.sleep(0.5)
    pass

# clean up
def cleanup():
    print("\nCleaning up...")
    light_off()
    GPIO.cleanup()
    print("Quit...")
    
# main loop
def main():
    print("Initializing...")
    init()
    print("Intialization complete...\n")
    while True:
        read_touchsensor()
        time.sleep(.5)

if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass
    pass

cleanup()
