//Successfully prints but only prints 0's, no real values

#include <dht.h>

#define dataPin 4 // Defines pin number to which the sensor is connected
dht sensor; // Creats a DHT object
//int dataPin = A0;

void setup() {
  Serial.begin(9600);

}
void loop() {
  delay(1000);
  int readData = sensor.read11(dataPin); // Reads the data from the sensor
  float t = sensor.temperature; // Gets the values of the temperature
  float h = sensor.humidity; // Gets the values of the humidity
  
  // Printing the results on the serial monitor
  Serial.print("Temperature = ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print("    Humidity = ");
  Serial.print(h);
  Serial.println(" % ");
  Serial.print("\n");
  
  delay(5000); // Delays 5 secods
}
//Code language: Arduino (arduino)
