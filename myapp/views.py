import random
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .models import SensorReading
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import paho.mqtt.client as mqtt
from .mqtt_handler import MQTTClient
import json
from paho.mqtt import client as mqtt_client

# Create your views here.

import paho.mqtt.client as mqtt

# Callback function when connection is established
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic
    client.subscribe("aswar")

# Callback function when a message is received
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    pairs = payload.split(',')
    full = {}
    for pair in pairs:
        try:
            key, value = pair.split(':')
            key = key.strip().strip('"')
            value = value.strip().strip('"')
            full[key] = value
        except ValueError:
            print(f"Invalid key-value pair: {pair}")
    tempC = full['{"tempC']
    tempF = str((float(tempC)*9 /5) + 32)
    dsm_consentrate = full['dsm_consentrate']
    dsm_particle = full['dsm_particle']
    air_quality_label = full['air_quality_label']
    sensor_value = full['sensor_value']
    print(tempC)
    print(tempF)
    print(dsm_consentrate)
    print(dsm_particle)
    print(air_quality_label)
    print(float(sensor_value))



client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("91.121.93.94", 1883, 60)

client.loop_forever()
SensorReading.objects.create()

def index(request):
    return render(request, 'index.html')
