# sender_with_gui.py
import paho.mqtt.client as mqtt
import PySimpleGUI as sg
import time

# MQTT broker details
broker_address = "mqtt-dashboard.com"
broker_port = 1883

# Create an MQTT client instance
client = mqtt.Client(client_id="PC")

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

client.connect(broker_address, broker_port)

# GUI layout
layout = [
    [sg.Text("Enter Temperature: "), sg.InputText(key="-TEMP-")],
    [sg.Button("Send"), sg.Quit()]
]

window = sg.Window("Temperature Sender", layout)

client.loop_start()

while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, "Quit", "Cancel"):
        break

    if event == "Send":
        temp = values["-TEMP-"]
        topic = "testtopic/2"
        client.publish(topic, temp)

window.close()
