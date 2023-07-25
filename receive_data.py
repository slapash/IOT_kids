import paho.mqtt.client as mqtt

global temp 
# fonction callback quand on se connecte au broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # abonnement au sujet apres connexion
        client.subscribe("testtopic/2")  #S'abonner à un sujet
    else:
        print("Failed to connect, return code: ", rc)

# fonction callback quand on reçoit un message
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    temp = (str(message.payload.decode("utf-8")))

# infos broker
broker_address = "mqtt-dashboard.com"  # adresse du broker
broker_port = 1883  # prt mqtt 1883 TCP 8884 Websocket

# Création d'une instance MQTT
client = mqtt.Client(client_id="PC_receveur")  # Replace with your desired client ID

# mettre en place les callbacks
client.on_connect = on_connect
client.on_message = on_message


# connexion au broker
client.connect(broker_address, broker_port)

#Boucle qui captent les messages
client.loop_forever()
