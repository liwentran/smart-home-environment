import sensors
from time import sleep

# main loop
def main():
    sensors.init()
    touch_sensor = sensors.Touch(26)
    light = sensors.LED(18)
    light.blink_once()
    
    while True:
        print(touch_sensor)
        sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


sensors.cleanup()
