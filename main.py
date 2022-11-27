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
    #keadaan baris 1
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_1 = True
    else:
        keadaansoil_1 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_1 = True
    else:
        keadaansuhu_1 = False

    #keadaan baris 2
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_2 = True
    else:
        keadaansoil_2 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_2 = True
    else:
        keadaansuhu_2 = False
    
    #keadaan baris 3
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_3 = True
    else:
        keadaansoil_3 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_3 = True
    else:
        keadaansuhu_3 = False

    #keadaan baris 4
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_4 = True
    else:
        keadaansoil_4 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_4 = True
    else:
        keadaansuhu_4 = False

    #keadaan baris 5
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_5 = True
    else:
        keadaansoil_5 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_5 = True
    else:
        keadaansuhu_5 = False

    #keadaan baris 6
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_6 = True
    else:
        keadaansoil_6 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_6 = True
    else:
        keadaansuhu_6 = False

    #keadaan baris 7
    if float(data_sensor_soil[0]) <= 50:
        keadaansoil_7 = True
    else:
        keadaansoil_7 = False

    if float(data_sensor_suhu[0]) >= 30:
        keadaansuhu_7 = True
    else:
        keadaansuhu_7 = False

    #baris 1
    if  keadaansoil_1 == True & keadaansuhu_1 == True:
        pinSelenoid_1.write(hidup)
        data_sensor_solenoid_1 = True
        print("hidup")
    else:
        pinSelenoid_1.write(mati)
        data_sensor_solenoid_1 = False
    
    #baris 2
    if keadaansoil_2 == True & keadaansuhu_2 == True:
        pinSelenoid_2.write(hidup)
        data_sensor_solenoid_2 = True
        print("hidup")
    else:
        pinSelenoid_2.write(mati)
        data_sensor_solenoid_2 = False
    
    #baris 3
    if keadaansoil_3 == True & keadaansuhu_3 == True:
        pinSelenoid_3.write(hidup)
        data_sensor_solenoid_3 = True
        print("hidup")
    else:
        pinSelenoid_3.write(mati)
        data_sensor_solenoid_3 = False
    
    #baris 4
    if keadaansoil_4 == True & keadaansuhu_4 == True:
        pinSelenoid_4.write(hidup)
        data_sensor_solenoid_4 = True
        print("hidup")
    else:
        pinSelenoid_4.write(mati)
        data_sensor_solenoid_4 = False
    
    #baris 5
    if keadaansoil_5 == True & keadaansuhu_5 == True:
        pinSelenoid_5.write(hidup)
        data_sensor_solenoid_5 = True
        print("hidup")
    else:
        pinSelenoid_5.write(mati)
        data_sensor_solenoid_5 = False
    
    #baris 6
    if keadaansoil_6 == True & keadaansuhu_6 == True:
        pinSelenoid_6.write(hidup)
        data_sensor_solenoid_6 = True
        print("hidup")
    else:
        pinSelenoid_6.write(mati)
        data_sensor_solenoid_6 = False
    
    #baris 7
    if keadaansoil_7 == True & keadaansuhu_7 == True:
        pinSelenoid_7.write(hidup)
        data_sensor_solenoid_7 = True
        print("hidup")
    else:
        pinSelenoid_7.write(mati)
        data_sensor_solenoid_7 = False
    
    #upload data
    uploadDataSolenoid( 
        data_sensor_solenoid_1,
        data_sensor_solenoid_2,
        data_sensor_solenoid_3,
        data_sensor_solenoid_4,
        data_sensor_solenoid_5,
        data_sensor_solenoid_6,
        data_sensor_solenoid_7
    )




