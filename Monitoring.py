import paho.mqtt.client as mqtt
import time

broker_ip = "172.20.10.8"  # Replace with broker Pi's IP
topic = "test/flood"

def on_message(client, userdata, msg):
    print(f"Received message of size {len(msg.payload)} on topic {msg.topic}")

client = mqtt.Client()
client.on_message = on_message
client.connect(broker_ip, 1883, 60)
client.subscribe(topic)

print("Monitoring incoming MQTT messages...")
client.loop_forever()
