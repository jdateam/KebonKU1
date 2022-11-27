const int dry = 595;
const int wet = 239;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorVal = analogRead(A0);
  int percentageHumididy = map(sensorVal,  wet, dry, 100, 0);
  int sensorVal1 = analogRead(A1);
  int percentageHumididy1 = map(sensorVal1,  wet, dry, 100, 0);
  int sensorVal2 = analogRead(A2);
  int percentageHumididy2 = map(sensorVal2,  wet, dry, 100, 0);
  int sensorVal3 = analogRead(A3);
  int percentageHumididy3 = map(sensorVal3,  wet, dry, 100, 0);
  int sensorVal4 = analogRead(A4);
  int percentageHumididy4 = map(sensorVal4,  wet, dry, 100, 0);
  int sensorVal5 = analogRead(A5);
  int percentageHumididy5 = map(sensorVal5,  wet, dry, 100, 0);
  int sensorVal6 = analogRead(A6);
  int percentageHumididy6 = map(sensorVal6,  wet, dry, 100, 0);
  int sensorVal7 = analogRead(A7);
  int percentageHumididy7 = map(sensorVal7,  wet, dry, 100, 0);
  int sensorVal8 = analogRead(A8);
  int percentageHumididy8 = map(sensorVal8,  wet, dry, 100, 0);
  int sensorVal9 = analogRead(A9);
  int percentageHumididy9 = map(sensorVal9,  wet, dry, 100, 0);
   
  Serial.print(percentageHumididy);
  Serial.print(" ");
  Serial.print(percentageHumididy1);
  Serial.print(" ");
  Serial.print(percentageHumididy2);
  Serial.print(" ");
  Serial.print(percentageHumididy3);
  Serial.print(" ");
  Serial.print(percentageHumididy4);
  Serial.print(" ");
  Serial.print(percentageHumididy5);
  Serial.print(" ");
  Serial.print(percentageHumididy6);
  Serial.print(" ");
  Serial.print(percentageHumididy7);
  Serial.print(" ");
  Serial.print(percentageHumididy8);
  Serial.print(" ");
  Serial.print(percentageHumididy9);
  Serial.println(" ");
  
  delay(1000);
}
