import sensors
from time import sleep
import RPi.GPIO as GPIO

# main loop
def main():
    sensors.init()
    adc = sensors.MCP3008()
    touch_sensor = sensors.Touch(26)
    light = sensors.LED(18)
    light.blink_once()
    GPIO.setup(4, GPIO.IN)

    
    while True:
        print(touch_sensor)
        print("photo sensor: ")
        print(adc.read(channel = 0))
        print("fire: ")
        print(adc.read(channel = 1))
        sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


sensors.cleanup()
