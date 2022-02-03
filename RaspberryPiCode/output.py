import sensors
import dht11
from time import sleep
import RPi.GPIO as GPIO
import smoke_detector

# main loop
def main():
    sensors.init()
    adc = sensors.MCP3008()
    touch_sensor = sensors.Touch(26)
    light = sensors.LED(18)
    temp_and_humid = dht11.DHT11(pin = 14)
    light.blink_once()
    GPIO.setup(4, GPIO.IN)

    count = 0
    
    while True:
        print(touch_sensor)
        print("Light Level: ", adc.read(channel = 0))
        print("Fire: ", adc.read(channel = 1))
        print("Gas: ", adc.read(channel = 2))
        print("Water Level: ", adc.read(channel = 3))
        print("Vibration: ", adc.read(channel = 4))
        #online datasheet indicates that dht11 has a 6 second response time        
        if (count % 2 == 0):
            result = temp_and_humid.read()
            print("Temp: ", result.temperature, "C", " Humidity: ", result.humidity, "%", sep = "")

        print()
        count += 1
        
        sleep(3)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


sensors.cleanup()
