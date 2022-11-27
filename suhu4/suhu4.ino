#include <OneWire.h> //Memanggil library OneWire yang diperlukan sebagai dependensi library Dallas Temperature
#include <DallasTemperature.h> // Memanggil library Dallas Temperature
#define ONE_WIRE_BUS 6  // Menempatkan PIN hasil pembacaan sensor DS18B20 pada PIN 2. 
   //Disebut One Wire karena kita bisa menempatkan sensor DS18B20 lain pada PIN yang sama  

OneWire oneWire(ONE_WIRE_BUS); //Membuat variabel oneWire berdasarkan PIN yang telah didefinisikan
DallasTemperature sensor(&oneWire); //Membuat variabel untuk menyimpan hasil pengukuran

//deklarasi variable suhu DS18B20 dengan jenis data float
float suhuDS18B20_0;
float suhuDS18B20_1;
float suhuDS18B20_2;
float suhuDS18B20_3;

void setup(void)
{
  Serial.begin(9600); //Menginisiasikan setup kecepatan komunikasi
  sensor.begin();      //Menginisiasikan sensor One-Wire DS18B20

  // Sebelum melakukan pengukuran, atur resolusinya
  //sensor.setResolution(0, 9);  
  //sensor.setResolution(0, 10);
  //sensor.setResolution(0, 11);
  sensor.setResolution(0, 9);

  //sensor.setResolution(1, 9);  
  //sensor.setResolution(1, 10);
  //sensor.setResolution(1, 11);
  sensor.setResolution(1, 9);

  //sensor.setResolution(2, 9);  
  //sensor.setResolution(2, 10);
  //sensor.setResolution(2, 11);
  sensor.setResolution(2, 9);

  //sensor.setResolution(3, 9);  
  //sensor.setResolution(3, 10);
  //sensor.setResolution(3, 11);
  sensor.setResolution(3, 9);
  
}

void loop(void)
{
  
  sensor.requestTemperatures();  // Perintah konversi suhu
  //Membaca data suhu dari sensor #0 dan mengkonversikannya ke nilai Celsius
  suhuDS18B20_0 = sensor.getTempCByIndex(0);
  suhuDS18B20_1 = sensor.getTempCByIndex(1);
  suhuDS18B20_2 = sensor.getTempCByIndex(2);
  suhuDS18B20_3 = sensor.getTempCByIndex(3);    
  // suhuDS18B20 = (suhuDS18B20*9/5) + 32;
  // suhuDS18B20 = suhuDS18B20 = 273.15;

  //Serial.println(suhuDS18B20, 1);  //Presisi 1 digit
  //Serial.println(suhuDS18B20, 2);  //Presisi 2 digit
  //Serial.println(suhuDS18B20, 3);  //Presisi 3 digit
  Serial.print(suhuDS18B20_0, 1);  //Presisi 4 digit
  Serial.print(" ");

  //Serial.println(suhuDS18B20, 1);  //Presisi 1 digit
  //Serial.println(suhuDS18B20, 2);  //Presisi 2 digit
  //Serial.println(suhuDS18B20, 3);  //Presisi 3 digit
  Serial.print(suhuDS18B20_1, 1);  //Presisi 4 digit
  Serial.print(" ");

  //Serial.println(suhuDS18B20, 1);  //Presisi 1 digit
  //Serial.println(suhuDS18B20, 2);  //Presisi 2 digit
  //Serial.println(suhuDS18B20, 3);  //Presisi 3 digit
  Serial.print(suhuDS18B20_2, 1);  //Presisi 4 digit
  Serial.print(" ");

  //Serial.println(suhuDS18B20, 1);  //Presisi 1 digit
  //Serial.println(suhuDS18B20, 2);  //Presisi 2 digit
  //Serial.println(suhuDS18B20, 3);  //Presisi 3 digit
  Serial.print(suhuDS18B20_3, 1);  //Presisi 4 digit
  Serial.println(" ");
  delay(1000);    //delay 1 detik (1000 miliseconds)
}
