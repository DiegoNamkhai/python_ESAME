import mysql.connector
import json
import requests
import time
from datetime import date
from datetime import datetime


class value:
  STR_DATA_OSSERVAZIONE = ""
  NOME_STAZIONE = ""
  NO2 = ""
  O3 = ""
  SO2 = ""
  H2S = ""
  BENZENE = ""
  VALIDAZIONE = ""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sensoristica_esame"
)

cn = mydb.cursor()

sql = "SELECT nomeP FROM postazione"
#val = (app.nome,app.dato,app.valore,app.data)
cn.execute("SELECT nomeP FROM postazione")
#mydb.commit()

myresult = cn.fetchall()
today = date.today()
d1 = today.strftime("%d-%m-%Y")
app = []
z=0
for x in myresult:
  response = requests.get('http://www.arpat.toscana.it/temi-ambientali/aria/qualita-aria/dati_orari_real_time/json_orari_nrt/' + x[0] +'/19-05-2021')
  dat = json.loads(response.text)
  i=0
  app2 = []
  max = datetime.strptime("01-01-2002 00", "%d-%m-%Y %H")
  for y in dat:
    data = value()
    data.STR_DATA_OSSERVAZIONE =dt_object2 = datetime.strptime(dat[i]['STR_DATA_OSSERVAZIONE'], "%d-%m-%Y %H")
    print("STR_DATA_OSSERVAZIONE "+ str(data.STR_DATA_OSSERVAZIONE))
    data.NOME_STAZIONE = dat[i]['NOME_STAZIONE']
    print("NOME_STAZIONE "+ data.NOME_STAZIONE)
    data.NO2 = dat[i]['NO2']
    print("NO2 ")
    print(data.NO2)
    data.O3 = dat[i]['O3']
    print("O3 ")
    print(data.O3)
    data.SO2 = dat[i]['SO2']
    print("SO2 ")
    print(data.SO2)
    data.H2S = dat[i]['H2S']
    print("H2S ")
    print(data.H2S)
    data.BENZENE = dat[i]['BENZENE']
    print("BENZENE ")
    print(data.BENZENE)
    data.VALIDAZIONE = dat[i]['VALIDAZIONE']
    print("VALIDAZIONE "+ data.VALIDAZIONE)
    print("i")
    print(i)
    if(data.STR_DATA_OSSERVAZIONE > max):
      max = data.STR_DATA_OSSERVAZIONE
    app2.append(data)
    del data
    i += 1
  print(max)
  app.append(app2)
  app2.insert(0, max)
  del app2
  z += 1
print(app[0][0].strftime("%d-%m-%Y %H"))



    
  












