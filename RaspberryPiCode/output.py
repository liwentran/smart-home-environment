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

    
    while True:
        print(touch_sensor)
        print("photo sensor: ", adc.read(channel = 0))
        print("fire: ", adc.read(channel = 1))
        #print("temp and humid" , adc.read(channel = 2))
        result = temp_and_humid.read()
        print("Temp: ", result.temperature, "C", " Humidity: ", result.humidity, "%", sep = "")
        print("Smoke/gas?: ", adc.read(channel = 3));
        print()
        sleep(3)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


sensors.cleanup()
