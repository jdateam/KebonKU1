const int ph_Pin = A0;
const int ph_Pin_satu = A1;
const int ph_Pin_dua = A2;
const int ph_Pin_tiga = A3;
const int ph_Pin_empat = A4;
const int ph_Pin_lima = A5;
const int ph_Pin_enam = A6;
const int ph_Pin_tujuh = A7;
const int ph_Pin_delapan = A8;
const int ph_Pin_sembilan = A9;

float Po_satu = 0;
float Po_dua = 0;
float Po_tiga = 0;
float Po_empat = 0;
float Po_lima = 0;
float Po_enam = 0;
float Po_tujuh = 0;
float Po_delapan = 0;
float Po_sembilan = 0;
float Po = 0;

float PH_step;
float PH_step_satu;
float PH_step_dua;
float PH_step_tiga;
float PH_step_empat;
float PH_step_lima;
float PH_step_enam;
float PH_step_tujuh;
float PH_step_delapan;
float PH_step_sembilan;

int nilai_analog_PH;
int nilai_analog_PH_satu;
int nilai_analog_PH_dua;
int nilai_analog_PH_tiga;
int nilai_analog_PH_empat;
int nilai_analog_PH_lima;
int nilai_analog_PH_enam;
int nilai_analog_PH_tujuh;
int nilai_analog_PH_delapan;
int nilai_analog_PH_sembilan;

double TeganganPh;
double TeganganPh_satu;
double TeganganPh_dua;
double TeganganPh_tiga;
double TeganganPh_empat;
double TeganganPh_lima;
double TeganganPh_enam;
double TeganganPh_tujuh;
double TeganganPh_delapan;
double TeganganPh_sembilan;

float PHempat = 3.1;
float PHtujuh = 2.6;

void setup(){
  pinMode (ph_Pin, INPUT);
  pinMode (ph_Pin_satu, INPUT);
  pinMode (ph_Pin_dua, INPUT);
  pinMode (ph_Pin_tiga, INPUT);
  pinMode (ph_Pin_empat, INPUT);
  pinMode (ph_Pin_lima, INPUT);
  pinMode (ph_Pin_enam, INPUT);
  pinMode (ph_Pin_tujuh, INPUT);
  pinMode (ph_Pin_delapan, INPUT);    
  pinMode (ph_Pin_sembilan, INPUT);
  Serial.begin(9600);
}

void loop(){
  nilai_analog_PH = analogRead(ph_Pin);
  TeganganPh = 5 / 1024.0 * nilai_analog_PH;
  PH_step = (PHempat - PHtujuh) / 3;
  Po = 7.00 + ((PHtujuh - TeganganPh) / PH_step);

  nilai_analog_PH_satu = analogRead(ph_Pin_satu);
  TeganganPh_satu = 5 / 1024.0 * nilai_analog_PH_satu;
  PH_step_satu = (PHempat - PHtujuh) / 3;
  Po_satu = 7.00 + ((PHtujuh - TeganganPh_satu) / PH_step_satu);

  nilai_analog_PH_dua = analogRead(ph_Pin_dua);
  TeganganPh_dua = 5 / 1024.0 * nilai_analog_PH_dua;
  PH_step_dua = (PHempat - PHtujuh) / 3;
  Po_dua = 7.00 + ((PHtujuh - TeganganPh_dua) / PH_step_dua);

  nilai_analog_PH_tiga = analogRead(ph_Pin_tiga);
  TeganganPh_tiga = 5 / 1024.0 * nilai_analog_PH_tiga;
  PH_step_tiga = (PHempat - PHtujuh) / 3;
  Po_tiga = 7.00 + ((PHtujuh - TeganganPh) / PH_step_tiga);

  nilai_analog_PH_empat = analogRead(ph_Pin_empat);
  TeganganPh_empat = 5 / 1024.0 * nilai_analog_PH_empat;
  PH_step_empat = (PHempat - PHtujuh) / 3;
  Po_empat = 7.00 + ((PHtujuh - TeganganPh_empat) / PH_step_empat);

  nilai_analog_PH_lima = analogRead(ph_Pin_lima);
  TeganganPh_lima = 5 / 1024.0 * nilai_analog_PH_lima;
  PH_step_lima = (PHempat - PHtujuh) / 3;
  Po_lima = 7.00 + ((PHtujuh - TeganganPh_lima) / PH_step_lima);

  nilai_analog_PH_enam = analogRead(ph_Pin_enam);
  TeganganPh_enam = 5 / 1024.0 * nilai_analog_PH_enam;
  PH_step_enam = (PHempat - PHtujuh) / 3;
  Po_enam = 7.00 + ((PHtujuh - TeganganPh_enam) / PH_step_enam);

  nilai_analog_PH_tujuh = analogRead(ph_Pin_tujuh);
  TeganganPh_tujuh = 5 / 1024.0 * nilai_analog_PH_tujuh;
  PH_step_tujuh = (PHempat - PHtujuh) / 3;
  Po_tujuh = 7.00 + ((PHtujuh - TeganganPh_tujuh) / PH_step_tujuh);

  nilai_analog_PH_delapan = analogRead(ph_Pin_delapan);
  TeganganPh_delapan = 5 / 1024.0 * nilai_analog_PH_delapan;
  PH_step_delapan = (PHempat - PHtujuh) / 3;
  Po_delapan = 7.00 + ((PHtujuh - TeganganPh_delapan) / PH_step_delapan);

  nilai_analog_PH_sembilan = analogRead(ph_Pin_sembilan);
  TeganganPh_sembilan = 5 / 1024.0 * nilai_analog_PH_sembilan;
  PH_step_sembilan = (PHempat - PHtujuh) / 3;
  Po_sembilan = 7.00 + ((PHtujuh - TeganganPh) / PH_step_sembilan);

  Serial.print(Po, 2);
  Serial.print(" ");
  Serial.print(Po_satu, 2);
  Serial.print(" ");
  Serial.print(Po_dua, 2);
  Serial.print(" ");
  Serial.print(Po_tiga, 2);
  Serial.print(" ");
  Serial.print(Po_empat, 2);
  Serial.print(" ");
  Serial.print(Po_lima, 2);
  Serial.print(" ");
  Serial.print(Po_enam, 2);
  Serial.print(" ");
  Serial.print(Po_tujuh, 2);
  Serial.print(" ");
  Serial.print(Po_delapan, 2);
  Serial.print(" ");
  Serial.print(Po_sembilan, 2);
  Serial.println(" ");
  delay(1000);
}
