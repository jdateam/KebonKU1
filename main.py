import serial
from model import uploadDataSoil
from model import uploadDataPh
from model import uploadDataSuhu
from model import uploadDataSolenoid
from pyfirmata import ArduinoMega

serial_soil = serial.Serial("COM9", 9600)
serial_ph = serial.Serial("COM10", 9600)
serial_suhu = serial.Serial("COM11", 9600)

#Solenoid 
hidup = 0
mati = 1

board = ArduinoMega('COM12')
# board = ArduinoMega('COM9')

pinSelenoid_1 = board.get_pin('d:4:o')
pinSelenoid_2 = board.get_pin('d:5:o')
pinSelenoid_3 = board.get_pin('d:6:o')
pinSelenoid_4 = board.get_pin('d:7:o')
pinSelenoid_5 = board.get_pin('d:8:o')
pinSelenoid_6 = board.get_pin('d:9:o')
pinSelenoid_7 = board.get_pin('d:10:o')
pinSelenoid_8 = board.get_pin('d:11:o')

#Solenoid dalam keadaan mati
pinSelenoid_1.write(mati)
pinSelenoid_2.write(mati)
pinSelenoid_3.write(mati)
pinSelenoid_4.write(mati)
pinSelenoid_5.write(mati)
pinSelenoid_6.write(mati)
pinSelenoid_7.write(mati)
pinSelenoid_8.write(mati)


# looping dimulai
while True:
    line_soil = serial_soil.readline()
    line_ph = serial_ph.readline()
    line_suhu = serial_suhu.readline()

    data_soil = line_soil.decode()
    data_ph = line_ph.decode()
    data_suhu = line_suhu.decode()

    data_sensor_soil = data_soil.split()
    data_sensor_ph = data_ph.split()
    data_sensor_suhu = data_suhu.split()

    print(data_sensor_soil)

    uploadDataSoil(
        data_sensor_soil[0], 
        data_sensor_soil[1],
        data_sensor_soil[2],
        data_sensor_soil[3],
        data_sensor_soil[4],
        data_sensor_soil[5],
        data_sensor_soil[6],
        data_sensor_soil[7],
        data_sensor_soil[8],
    )

    print(data_sensor_ph)

    uploadDataPh(
        data_sensor_ph[0], 
        data_sensor_ph[1],
        data_sensor_ph[2],
        data_sensor_ph[3],
        data_sensor_ph[4],
        data_sensor_ph[5],
        data_sensor_ph[6],
        data_sensor_ph[7],
        data_sensor_ph[8],
    )

    print(data_sensor_suhu)

    uploadDataSuhu(
        data_sensor_suhu[0], 
        data_sensor_suhu[1],
        data_sensor_suhu[2],
        data_sensor_suhu[3],
      #  data_sensor_suhu[4],
       # data_sensor_suhu[5],
       # data_sensor_suhu[6],
       # data_sensor_suhu[7],
       # data_sensor_suhu[8],
    )
# batas sensor
    

#penyiraman otomatis
    #baris 1
    if  True:#float(data_sensor_soil[0]) <= 50 & float(data_sensor_suhu[0]) >= 30:
        pinSelenoid_1.write(hidup)
        data_sensor_solenoid_1 = True
        print("hidup")
    else:
        pinSelenoid_1.write(mati)
        data_sensor_solenoid_1 = False
    
    #baris 2
    if True:#float(data_sensor_soil[1]) <= 50 & float(data_sensor_suhu[1]) >= 30:
        pinSelenoid_2.write(hidup)
        data_sensor_solenoid_2 = True
        print("hidup")
    else:
        pinSelenoid_2.write(mati)
        data_sensor_solenoid_2 = False
    
    #baris 3
    if True:#float(data_sensor_soil[2]) <= 50 & float(data_sensor_suhu[2]) >= 30:
        pinSelenoid_3.write(hidup)
        data_sensor_solenoid_3 = True
        print("hidup")
    else:
        pinSelenoid_3.write(mati)
        data_sensor_solenoid_3 = False
    
    #baris 4
    if True:#float(data_sensor_soil[3]) <= 50 & float(data_sensor_suhu[3]) >= 30:
        pinSelenoid_4.write(hidup)
        data_sensor_solenoid_4 = True
        print("hidup")
    else:
        pinSelenoid_4.write(mati)
        data_sensor_solenoid_4 = False
    
    #baris 5
    if True:#float(data_sensor_soil[4]) <= 50 & float(data_sensor_suhu[4]) >= 30:
        pinSelenoid_5.write(hidup)
        data_sensor_solenoid_5 = True
        print("hidup")
    else:
        pinSelenoid_5.write(mati)
        data_sensor_solenoid_5 = False
    
    #baris 6
    if True:#float(data_sensor_soil[5]) <= 50 & float(data_sensor_suhu[5]) >= 30:
        pinSelenoid_6.write(hidup)
        data_sensor_solenoid_6 = True
        print("hidup")
    else:
        pinSelenoid_6.write(mati)
        data_sensor_solenoid_6 = False
    
    #baris 7
    if True:#float(data_sensor_soil[6]) <= 50 & float(data_sensor_suhu[6]) >= 30:
        pinSelenoid_7.write(hidup)
        data_sensor_solenoid_7 = True
        print("hidup")
    else:
        pinSelenoid_7.write(mati)
        data_sensor_solenoid_7 = False

    #baris 8
    if True:#float(data_sensor_soil[7]) <= 50 & float(data_sensor_suhu[7]) >= 30:
        pinSelenoid_8.write(hidup)
        data_sensor_solenoid_8 = True
        print("hidup")
    else:
        pinSelenoid_8.write(mati)
        data_sensor_solenoid_8 = False
    
    
    
    #upload data
    uploadDataSolenoid( 
        data_sensor_solenoid_1,
        data_sensor_solenoid_2,
        data_sensor_solenoid_3,
        data_sensor_solenoid_4,
        data_sensor_solenoid_5,
        data_sensor_solenoid_6,
        data_sensor_solenoid_7,
        data_sensor_solenoid_8,
    )





