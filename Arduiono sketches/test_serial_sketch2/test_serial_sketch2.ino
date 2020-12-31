float val1 = 0.1234; 
float val2 = 50.1234;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  val1++;
  val2--;
  
  Serial.print(val1,4);
  Serial.print(";");
  Serial.println(val2,4);
  
  delay (100);

}
