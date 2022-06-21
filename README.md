# Cancom / Cisco - DevNet Express Meraki 
## Lab Training

für das Training könnt ihr euch bitte alle Lib´s aus der requirements.txt Datei installieren.

```shell
pip install -r requirements.txt
```



### Mittwoch Session 16:20 Uhr
Meraki MT Sensor overview with all auto generated for uses cases

In der ersten Aufgabe fragen wir die Meraki API nach der Temperatur des jeweiligen Sensors in eurer Meraki Organisation.

Den fertigen Code für die erste Aufgabe findet ihr in der Datei 
```
Temperatur.py
```
Hier bitte die Network ID mit der von euch tauschen. Achtet auch, dass ihr den richtigen Meraki Access Token als Umgebungsvariable setzt. Die **Serial** Number des Sensors im Querystring muss angepasst werden.

Die Ausgabe der Daten mitels Figlet ist nur eine optionale Spielerei:
```Python
# Ausgabe der Daten 
f = Figlet(font='banner3')
cls()
print (f.renderText(Temp))
print ('\nTEMP MIN')
print (f.renderText(Tempmin))
print ('\nTEMP MAX')
print (f.renderText(Tempmax))
```

so sollte es nun aussehen:
<p align="center"> 
<img src="./Temperatur.jpg">
</p>



### Donnerstag Session 9:30 Uhr
Create a Webhook receiver for alarm messagges from Meraki IoT devices.

Die zweite Aufgabe umfasst 
* das Anlegen eines Webhooks im Meraki Dashboard
* das Aufsezen eines Webservers, der auf die Events des Webhook hört und diese Ausgibt
* das Nutzen von NGROK als Tunel Dienst zu eurem Webserver



### Donnerstag Session 10:45 Uhr
Providing messages to Webex Teams/alarm spaces

