import json
import requests
import urllib3
import os
from pyfiglet import Figlet

# Meraki Token aus Umgebungsvariable lesen
token = os.getenv('MERAKI_DASHBOARD_API_KEY')

# Cear Screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# disable warnings about   using certificate verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
 'X-Cisco-Meraki-API-Key': token,
 'content-type': "application/json"
}

# Abfrage der Sensor Daten
querystring = {
    "metric":"temperature",
    "serials[]":["Q3CA-JY3L-GADC"]
}
sensors = requests.get('https://api.meraki.com/api/v1/networks/L_614741349136072803/sensor/stats/historicalBySensor', headers=headers, verify=False, params=querystring)
sensors = sensors.json()
# print (sensors)

Temp = str(round(sensors[0]['latest']['value'], 2))
Tempmin = str(round(sensors[0]['min'], 2))
Tempmax = str(round(sensors[0]['max'], 2))

# Ausgabe der Daten 
f = Figlet(font='banner3')
cls()
print (f.renderText(Temp))
print ('\nTEMP MIN')
print (f.renderText(Tempmin))
print ('\nTEMP MAX')
print (f.renderText(Tempmax))
