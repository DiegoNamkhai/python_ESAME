import mysql.connector
import json
import requests
import time
from datetime import date
from datetime import datetime



def repeat():

  class value:
    STR_DATA_OSSERVAZIONE = ""
    NOME_STAZIONE = ""
    NO2 = None
    O3 = None
    CO = None
    SO2 = None
    H2S = None
    BENZENE = None
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
  maxDef = datetime.strptime("01-01-2002 00", "%d-%m-%Y %H")
  for x in myresult:
    response = requests.get('http://www.arpat.toscana.it/temi-ambientali/aria/qualita-aria/dati_orari_real_time/json_orari_nrt/' + x[0] +'/'+d1)
    dat = json.loads(response.text)
    i=0
    app2 = []
    max = maxDef
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
      data.CO = dat[i]['CO']
      print("CO ")
      print(data.CO)
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
    #print(max)
    app.append(app2)
    app2.insert(0, max)
    print("z" + str(z))
    print(app[z][0].strftime("%d-%m-%Y %H"))
    del app2
    z += 1

  #del cn
  #cn = mydb.cursor()
  #cn.cursor(buffered=True)
  k=0
  for x in myresult:
    sql = "SELECT MAX(dataRil) FROM campionamento WHERE postazione = '" + str(x[0]) +"'"
    val = (x[0])
    print(val)
    print (sql)
    cn.execute(sql)
    #mydb.commit()
    result = cn.fetchall()
    #print(app[k][0])
    if(app[k][0] != maxDef):
      print("result")
      print(result[0])
      if(result[0][0] != None):
        day = datetime.strptime(str(result[0][0]), "%Y-%m-%d %H:%M:%S")
        day = datetime.strptime(day.strftime("%d-%m-%Y %H"), "%d-%m-%Y %H")
        #print("day")
        #print(day)
        #print("day fetch")
        #print(app[k][0])
        if(app[k][0] > day):
          check = True
        else: check = False
      else: check = True   
      #print(check) 
      if(check):
        for m in range(1, len(app[k])):
              if(app[k][0] == app[k][m].STR_DATA_OSSERVAZIONE):
                temp = app[k][m]
                break    
        sql = "INSERT INTO `campionamento` (`postazione`, `IDcamp`, `dataRil`, `NO2`, `O3`, `CO`, `SO2`, `H2S`, `BENZENE`) VALUES (%s, NULL, %s, %s, %s, %s, %s, %s, %s)"
        day = datetime.strptime(temp.STR_DATA_OSSERVAZIONE.strftime("%Y-%m-%d %H"), "%Y-%m-%d %H")
        val = (temp.NOME_STAZIONE, day, temp.NO2, temp.O3, temp.CO, temp.SO2, temp.H2S, temp.BENZENE)
        cn.execute(sql,val)
        mydb.commit()
        print(cn.rowcount, "record inserted.")
        del day
        del temp
    k += 1


while True:
  repeat()
  time.sleep(12)









    
  












