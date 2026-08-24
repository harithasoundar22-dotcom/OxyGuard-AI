from flask import Flask, jsonify, render_template
import random
import datetime

app = Flask(__name__)

# Simulated live data

BASE_TIME = datetime.datetime.now()

WARD_STATUS = [
    {"ward": "ICU", "consumption": "185 L/hr", "status": "Normal", "risk": "🟢 Low"},
    {"ward": "Emergency", "consumption": "120 L/hr", "status": "High", "risk": "🟡 Medium"},
    {"ward": "OT", "consumption": "75 L/hr", "status": "Normal", "risk": "🟢 Low"},
    {"ward": "General Ward", "consumption": "65 L/hr", "status": "Normal", "risk": "🟢 Low"},
]

ALERTS = {
    "critical": [
        "Oxygen pressure critically low",
        "Estimated supply < 4 hours",
    ],
    "warning": [
        "Unusual consumption detected",
        "Supply expected to reach warning level",
    ],
    "information": [
        "Daily consumption increased by 8%",
    ],
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/dashboard")
def dashboard_api():
    now = datetime.datetime.now()
    live_data = {
        "oxygen_pressure": 8.2,
        "flow_rate": 420,
        "consumption": 385,
        "estimated_supply_hours": 14.6,
        "active_alerts": 2,
        "remaining_percent": 78,
        "available_liters": 7800,
        "predicted_consumption_rate": 535,
        "estimated_remaining_time": 14.6,
        "ai_recommendation": "Refill required within 10 hours.",
        "anomaly": {
            "label": "Abnormal Consumption Detected",
            "message": "ICU oxygen consumption is 32% above normal.",
            "confidence": 94,
            "status": "Investigating",
        },
        "forecast": {
            "next_4h": 1620,
            "next_12h": 4850,
            "next_24h": 9760,
            "peak_demand": "2:00 PM",
        },
        "ward_status": WARD_STATUS,
        "alerts": ALERTS,
        "workflow": "Sensors → ESP32 → Backend → Database → AI Models → Dashboard → Alerts",
        "ai_layer": [
            "Isolation Forest → Anomaly Detection",
            "XGBoost / Random Forest → Demand Prediction",
            "Prediction + Current Supply → Remaining-Time Estimation",
        ],
        "series": generate_series(now, 24),
    }
    return jsonify(live_data)

@app.route("/api/chart/<int:hours>")
def chart_api(hours):
    now = datetime.datetime.now()
    times, pressure, flow, consumption = generate_series(now, hours)
    return jsonify({
        "times": times,
        "oxygen_pressure": pressure,
        "flow_rate": flow,
        "consumption": consumption,
    })

@app.route("/api/summary")
def summary_api():
    return jsonify({
        "dashboard_deck": [
            {"label": "Oxygen Pressure", "value": "8.2 bar", "color": "green"},
            {"label": "Flow Rate", "value": "420 L/min", "color": "blue"},
            {"label": "Current Consumption", "value": "385 L/hr", "color": "yellow"},
            {"label": "Estimated Supply", "value": "14.6 hrs", "color": "green"},
            {"label": "Active Alerts", "value": "2", "color": "red"},
        ],
    })


def generate_series(base_time, hours):
    points = []
    pressure = []
    flow = []
    consumption = []
    times = []
    for i in range(hours * 4):
        ts = base_time - datetime.timedelta(minutes=15 * (hours * 4 - i - 1))
        times.append(ts.strftime("%H:%M"))
        pressure_val = round(7.8 + random.uniform(-0.3, 0.4), 2)
        flow_val = round(380 + random.uniform(-40, 50), 1)
        consumption_val = round(340 + random.uniform(-40, 60), 1)
        pressure.append(pressure_val)
        flow.append(flow_val)
        consumption.append(consumption_val)
    return times, pressure, flow, consumption

if __name__ == "__main__":
    app.run(debug=True)
