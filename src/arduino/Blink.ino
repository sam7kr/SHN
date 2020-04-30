
String  msg = "";

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0){
      msg = Serial.readString();
  }
  
  if (msg == "2on"){
    digitalWrite(2, HIGH); 
  }
  else if(msg == "2off"){
    digitalWrite(2, LOW);
  }
  else if (msg == "3on"){
    digitalWrite(3, HIGH); 
  }
  else if(msg == "3off"){
    digitalWrite(3, LOW);
  }
 
  delay(50);                
}
