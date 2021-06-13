float val = 0.1234; 

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  val++;
  Serial.println(val,4);
  delay (100);

}
