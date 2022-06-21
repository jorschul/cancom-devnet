import os
from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv #pip install python-dotenv
import json

load_dotenv() #lade environment Variablen aus Datei .env

webex_teams_access_token = os.getenv('WEBEX_TEAMS_ACCESS_TOKEN')

app = Flask(__name__)
api = WebexTeamsAPI(access_token=webex_teams_access_token)


def newWebexRoom():
    # finde alle Räume die im Titel "Meraki Alarm Room" haben und lösche diese
    all_rooms = api.rooms.list()
    alarm_rooms = [room for room in all_rooms if 'Meraki Alarm Room' in room.title]
    for room in alarm_rooms:
        api.rooms.delete(room.id)

    # erstelle einen neuen "Meraki Alarm Room" und füge Erik Thiele hinzu
    alarm_room = api.rooms.create('Meraki Alarm Room')
    api.memberships.create(alarm_room.id, personEmail="erik.thiele@cancom.de")
    return (alarm_room)


@app.route('/')
def index():
    return "<h1>Webserver is running...</h1>"


@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.json
    sharedsecret = json_data['sharedSecret']

    if sharedsecret == "12345678":
        OrgName = json_data['organizationName']
        NetworkName = json_data['networkName']
        deviceModel = json_data['deviceModel']
        deviceName = json_data['deviceName']
        deviceSerial = json_data['deviceSerial']

        print ("SharedSecret OK")
        print ("Device Model: " + deviceModel)

        if deviceModel == "MT20":
            dooropen = json_data['alertData']['triggerData'][0]['trigger']['sensorValue']
            if dooropen == 1:
                print ("Door open")
                api.messages.create(alarm_room.id, markdown="- - -\n **Door open** - "+deviceName)    
            elif dooropen == 0:
                print ("Door closed") 
                api.messages.create(alarm_room.id, markdown="- - -\n **Door closed** - "+deviceName)
            api.messages.create(alarm_room.id, markdown=">**Org:** "+OrgName+
                                "\n**Network:** "+NetworkName+
                                "\n**Device Model:** "+deviceModel+
                                "\n**deviceSerial:** "+deviceSerial)
    else:
        print ("SharedSecret False :" + sharedsecret)
    
    return "OK"

alarm_room = newWebexRoom()

app.run(host='0.0.0.0', port=80, threaded=True, debug=True)



