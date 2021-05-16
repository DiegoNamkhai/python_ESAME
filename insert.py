import mysql.connector
import json
import requests


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sensoristica_esame"
)

cn = mydb.cursor()

class value:
  nome = ""
  dato = ""
  valore = ""
  data = ""

day = "03-05-2021"
value.data = "2021-05-16 23"


response = requests.get('http://www.arpat.toscana.it/temi-ambientali/aria/qualita-aria/bollettini/bollettino_json/regionale/' + day)

data = json.loads(response.text)



i=0
app = value()
value = ("PM10", "PM2dot5", "NO2", "SO2", "CO" , "H2S" , "BENZENE")
while data[i]["PROVINCIA"] == "FIRENZE" :
  app.nome = data[i]["NOME_STAZIONE"]
  for x in value :
    if data[i][x] != "-" and data[i][x] != "n.d.":
      app.valore = data[i][x]
      app.dato = x
      print(app.nome)
      print(app.dato)
      print(app.valore)
      print(app.data)
      print("\n")
      sql = "INSERT INTO `campionamento` (`postazione`, `IDcamp`, `dato`, `valore`, `dataRil`) VALUES (%s, NULL, %s, %s, %s)"
      val = (app.nome,app.dato,app.valore,app.data)
      cn.execute(sql,val)
      mydb.commit()
  i += 1






  
 
