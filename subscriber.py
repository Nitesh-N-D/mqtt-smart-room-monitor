import paho.mqtt.client as mqtt
import json

broker = "broker.hivemq.com"
topic = "nitesh/smartroom/data"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, 1883, 60)
client.subscribe(topic)

client.loop_forever()