import paho.mqtt.client as mqtt
import time
import random
import json

broker = "broker.hivemq.com"
topic = "nitesh/smartroom/data"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    data = {
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2)
    }
    client.publish(topic, json.dumps(data))
    print("Published:", data)
    time.sleep(5)