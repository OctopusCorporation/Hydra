int led = 13;

void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop()
{
  if(Serial.available() > 0)
  {
    int command = Serial.read();
    
    if(command == '1')
      digitalWrite(led, HIGH);
    else if(command == '0')
      digitalWrite(led, LOW);
  }
}
