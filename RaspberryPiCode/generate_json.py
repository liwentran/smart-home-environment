import sensors
import dht11
#contained in the Adafruit-Raspberry-Pi-Python-Code folder, but cannot be found
from time import sleep
import RPi.GPIO as GPIO
import smoke_detector
import json

# main lop
def main():
    generate()
    
def generate():
    sensors.init()

    adc = sensors.MCP3008()
    touch_sensor = sensors.Touch(26)
    light = sensors.LED(18)
    temp_and_humid = dht11.DHT11(pin = 14)
    GPIO.setup(4, GPIO.IN)

    

    light_level = adc.read(channel = 0)
    fire_sensor = adc.read(channel = 1)
    gas_sensor = adc.read(channel = 2) #MQ2 Gas Smoke Sensor
    water_level = adc.read(channel = 3)
    vibration_sensor = adc.read(channel = 4)
    sound_level = adc.read(channel = 5)
    carbon_monoxide = adc.read(channel = 7)
    
    result = temp_and_humid.read()
    temperature = result.temperature
    humidity = result.humidity
    
    # Data to be written
    dictionary ={
        "touch" : touch_sensor.get_state(),
        "lightlevel" : light_level,
        "fire" : fire_sensor,
        "gas" : gas_sensor,
        "waterlevel" : water_level,
        "vibration" : vibration_sensor,
        "soundlevel" : sound_level,
        "carbonmonoxide" : carbon_monoxide,
        "temperature" : temperature,
        "humidity" : humidity
    }

    # Serializing json 
    json_object = json.dumps(dictionary, indent = 4)

    print("writing file")
    # Writing to sample.json
    with open("sensor_data.json", "w") as outfile:
        outfile.write(json_object)
    print("written")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


sensors.cleanup()
