import firebase_admin
from firebase_admin import credentials, db


#menginisiasi pengenal database
# credential sertifikat didapat dari project view/ project setting/service account (paling bwh) 
cred = credentials.Certificate("authentication.json")
#database url didapat dari view/ project setting/general (di coding urlnya)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://kebonku-database-default-rtdb.asia-southeast1.firebasedatabase.app"
})
#membuat database soil 

def uploadDataSoil(soil_1, soil_2, soil_3, soil_4, soil_5, soil_6, soil_7, soil_8, soil_9):

    ref = db.reference('/')
    #cara set parent dari data
    ref.set({
        'Soil_moister':
            {
            #cara set child dari data
                'moister_1': int(soil_1),
                'moister_2': int(soil_2),
                'moister_3': int(soil_3),
                'moister_4': int(soil_4),
                'moister_5': int(soil_5),  
                'moister_6': int(soil_6),  
                'moister_7': int(soil_7),  
                'moister_8': int(soil_8),  
                'moister_9': int(soil_9)
            }
    })

def uploadDataPh(ph_meter_1, ph_meter_2, ph_meter_3, ph_meter_4, ph_meter_5, ph_meter_6, ph_meter_7, ph_meter_8, ph_meter_9):

    ref = db.reference('/')
    #cara set parent dari data
    ref.set({
        'Ph meter':
            {
            #cara set child dari data
                'Ph_meter_1': float(ph_meter_1),
                'Ph_meter_2': float(ph_meter_2),
                'Ph_meter_3': float(ph_meter_3),
                'Ph_meter_4': float(ph_meter_4),
                'Ph_meter_5': float(ph_meter_5),  
                'Ph_meter_6': float(ph_meter_6),  
                'Ph_meter_7': float(ph_meter_7),  
                'Ph_meter_8': float(ph_meter_8),  
                'Ph_meter_9': float(ph_meter_9)
            }
    })

def uploadDataSuhu(suhu_1, suhu_2, suhu_3, suhu_4):

    ref = db.reference('/')
    #cara set parent dari data
    ref.set({
        'Ph meter':
            {
            #cara set child dari data
                'Suhu_1': float(suhu_1),
                'Suhu_2': float(suhu_2),
                'Suhu_3': float(suhu_3),
                'Suhu_4': float(suhu_4),
               # 'Suhu_5': float(suhu_5),  
                #'Suhu_6': float(suhu_6),  
               # 'Suhu_7': float(suhu_7),  
               # 'Suhu_8': float(suhu_8),  
               # 'Suhu_9': float(suhu_9)
            }
    })

def uploadDataSolenoid(solenoid_1, solenoid_2, solenoid_3, solenoid_4, solenoid_5, solenoid_6, solenoid_7, solenoid_8):

    ref = db.reference('/')
    #cara set parent dari data
    ref.set({
        'Solenoid':
            {
            #cara set child dari data
                'Solenoi_1': float(solenoid_1),
                'Solenoid_2': float(solenoid_2),
                'Solenoid_3': float(solenoid_3),
                'Solenoid_4': float(solenoid_4),
                'Solenoid_5': float(solenoid_5),  
                'Solenoid_6': float(solenoid_6),  
                'Solenoid_7': float(solenoid_7),  
                'Solenoid_8': float(solenoid_8)
            }
    })

