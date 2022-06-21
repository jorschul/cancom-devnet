from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Webserver is running...</h1>"


@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.json
    sharedsecret = json_data['sharedSecret']

    #überprüfen, ob das Secret des Webhooks stimmt und dem Webhook vertraut werden kann
    if sharedsecret == "12345678":
        deviceModel = json_data['deviceModel']
        print ("SharedSecret OK")
        print ("Device Model: " + deviceModel)

        # Nur wenn es ein MT20 ist, wird der Sesnor Zustand (open / colosed) ausgegeben
        if deviceModel == "MT20":
            dooropen = json_data['alertData']['triggerData'][0]['trigger']['sensorValue']
            if dooropen == 1:
                print ("Door open")
            elif dooropen == 0:
                print ("Door closed") 
    else:
        print ("SharedSecret False :" + sharedsecret)
    
    return "OK"


# Starten des Webservers auf Port 80 -> NGROK muss auf Port 80 zeigen (NGROK http 80)
app.run(host='0.0.0.0', port=80, threaded=True, debug=True)