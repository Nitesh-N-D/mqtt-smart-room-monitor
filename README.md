# MQTT-Based Smart Room Monitoring System

## 📌 Project Overview
The **MQTT-Based Smart Room Monitoring System** is an industry-oriented Internet of Things (IoT) project that demonstrates real-time data communication using the **MQTT publish–subscribe protocol**. The system simulates smart room sensor data such as temperature and humidity, processes it using a cloud-hosted backend, and visualizes it through a real-time web dashboard deployed on **Microsoft Azure**.

This project is developed as part of the **Industry Oriented Course – Internet of Things**.

---

## 🎯 Objectives
- To understand and implement the MQTT protocol in IoT systems  
- To demonstrate asynchronous publish–subscribe communication  
- To design a real-time IoT monitoring dashboard  
- To deploy an IoT web application on cloud infrastructure  
- To gain hands-on experience with industry-relevant IoT architecture  

---

## 🧠 System Architecture
```
Sensor Simulator (Python)
        |
        | MQTT Publish
        v
MQTT Broker (HiveMQ Public)
        |
        | MQTT Subscribe
        v
Flask Backend (Azure Web App)
        |
        | AJAX / HTTP
        v
Web Dashboard (Browser)
```

---

## 🧰 Technology Stack
- **Protocol:** MQTT  
- **MQTT Broker:** HiveMQ Public Broker  
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Cloud Platform:** Microsoft Azure App Service (Free Tier)  
- **Version Control:** GitHub  

---

## 🌐 Live Deployment
🔗 **Azure Web App URL:**  
https://mqtt-smartroom-nitesh.azurewebsites.net

---

## ⚙️ Features
- Real-time temperature and humidity monitoring  
- MQTT-based publish–subscribe communication  
- Live updating graphs using Chart.js  
- AJAX-based auto-refresh without page reload  
- Threshold-based visual alerts  
- CSV data download for analysis  
- Cloud deployment using Azure App Service  

---

## ▶️ How to Run Locally

### Install dependencies
```
pip install -r requirements.txt
```

### Start the MQTT Publisher
```
python publisher.py
```

---

## 📚 Academic Relevance
This project aligns with the **Industry Oriented Course – Internet of Things** syllabus and covers IoT architecture, protocols, cloud deployment, and real-time data visualization.

---

## 🚀 Applications
- Smart home monitoring  
- Smart buildings  
- Industrial environment monitoring  
- Smart campuses  

---

## 🔮 Future Enhancements
- AI-based prediction models  
- ESP32 hardware integration  
- Mobile application support  
- Alert notifications  

---

## 👨‍💻 Author
**Nitesh N D**  
BE – Computer Science and Engineering  

---

## 📄 License
Educational use only.
