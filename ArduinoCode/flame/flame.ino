/* Fire sensor module test project
 * tutorial url: http://osoyoo.com/?p=671
 */
int Led=13; 
int buttonpin=3; 
int val; 
void setup(){
  pinMode(Led,OUTPUT); 
  pinMode(buttonpin,INPUT); 
}

void loop(){
  val=digitalRead(buttonpin); 
  if(val==LOW){
    digitalWrite(Led,HIGH); 
   }
  else
  {
    digitalWrite(Led,LOW); 
   }
}
