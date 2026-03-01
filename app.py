from flask import Flask, render_template, jsonify, send_file
import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime

app = Flask(__name__)

latest_data = {"temperature": "-", "humidity": "-"}
history = []

def on_message(client, userdata, msg):
    global latest_data, history
    data = json.loads(msg.payload.decode())
    latest_data = data

    history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "temperature": data["temperature"],
        "humidity": data["humidity"]
    })

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("nitesh/smartroom/data")
client.loop_start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    return jsonify(latest_data)

@app.route("/download")
def download_csv():
    filename = "smart_room_data.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["time", "temperature", "humidity"])
        writer.writeheader()
        writer.writerows(history)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)