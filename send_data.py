import paho.mqtt.client as mqtt
from serial_reader import readserial
import time

# MQTT broker details
broker_address = "mqtt-dashboard.com" 
broker_port = 1883  

# Create an MQTT client instance
client = mqtt.Client(client_id="PC")  # Id du client

#optionnel pour vérifier la connexion########################################
# Callback function when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code: ", rc)

# Callback function when the message is published to the broker
def on_publish(client, userdata, mid):
    print("Message published successfully!")

# Set the callbacks
client.on_connect = on_connect
client.on_publish = on_publish
##################################################

# Connect to the broker
client.connect(broker_address, broker_port)

# Your data to be sent
data_to_send = "Hello, MQTT Broker!"



# Loop to keep the client running (you can also use client.loop_forever() if you want to keep the script running)
client.loop_start()

while True:
    time.sleep(2)
    # Publish the data to a topic
    topic = "testtopic/2"  # Replace with your desired topic name
    client.publish(topic, readserial('COM10', 9600))