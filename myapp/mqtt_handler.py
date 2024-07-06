import paho.mqtt.client as mqtt
import json

class MQTTClient:
    def __init__(self, broker_address, broker_port, client_id):
        self.client = mqtt.Client(client_id)
        
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        self.client.connect(self.broker_address, self.broker_port)
        self.client.loop_start()  # Start loop to handle incoming messages

    # Rest of the MQTTClient class implementation...
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        # Subscribe to a specific topic upon connection
        self.client.subscribe("mytopic/test")

    def publish(self, topic, payload):
        self.client.publish(topic, json.dumps(payload))