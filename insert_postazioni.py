import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sensoristica_esame"
)

cn = mydb.cursor()

sql = "INSERT INTO `campionamento` (`postazione`, `IDcamp`, `dato`, `valore`, `unita`, `dataRil`) VALUES ('8', NULL, 'CO2', '440', 'PPM', CURRENT_TIMESTAMP)"
cn.execute(sql)

mydb.commit()