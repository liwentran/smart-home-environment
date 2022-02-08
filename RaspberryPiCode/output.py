import sensors
import dht11
from time import sleep
import RPi.GPIO as GPIO
import smoke_detector
#import carbon_monoxide

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
        print("Gas: ", adc.read(channel = 2)) #MQ2 Gas Smoke Sensor
        print("Water Level: ", adc.read(channel = 3))
        print("Vibration: ", adc.read(channel = 4))
        print("Sound Level: ", adc.read(channel = 5))
        print("Carbon Monoxide: ", adc.read(channel = 7))
        #online datasheet indicates that dht11 has a 6 second response time
        if (count % 2 == 0):
            result = temp_and_humid.read()
            print("Temp: ", result.temperature, "C", " Humidity: ", result.humidity, "%", sep = "")
        #if...
        #display AD value and CO density percent separately
        print()
        count += 1
        sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


sensors.cleanup()
