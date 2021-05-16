import requests

x = requests.get('http://www.arpat.toscana.it/temi-ambientali/aria/qualita-aria/dati_orari_real_time/json_orari_nrt/FI-GRAMSCI')
print(x.json())