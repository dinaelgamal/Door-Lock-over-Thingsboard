import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import tkinter as tk

ACCESS_TOKEN='7rMGBbig1bvx7697Xref'                 #Token of your device
broker="thingsboard.cloud"   			    #host name
port=1883 					    #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
client1.connect(broker,port,keepalive=60)

def ON():
    payload="{"
    payload+="\"Door \":Open"; 
    payload+="}"
    ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload)


def OFF():
    payload="{"
    payload+="\"Door \":Locked"; 
    payload+="}"
    ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    print(payload);

root = tk.Tk()
root.title("GUI")

onButton = tk.Button(root, text="ON", command=ON)
oFFButton = tk.Button(root, text="OFF", command=OFF)

onButton.pack()
oFFButton.pack()   


root.mainloop()