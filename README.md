# OxyGuard-AI
AI-powered hospital oxygen monitoring and prediction system
# OxyGuard AI

## AI-Powered Hospital Oxygen Monitoring and Prediction System

OxyGuard AI is an AI-powered hospital oxygen monitoring and prediction system designed to continuously monitor oxygen-related parameters and provide early warnings about abnormal consumption, possible leakage, and potential oxygen shortages.

## Problem Statement

Hospitals often depend on manual monitoring, pressure gauges, and basic threshold-based alarms for oxygen management. These methods mainly provide information about the current condition and may not identify abnormal consumption or potential shortages early enough.

## Proposed Solution

OxyGuard AI combines IoT sensors, cloud connectivity, and Artificial Intelligence to monitor oxygen systems in real time. The system analyzes sensor data to detect abnormal patterns, predict future oxygen demand, estimate remaining oxygen supply, and generate appropriate alerts.

## Key Features

* Real-time oxygen monitoring
* Oxygen pressure and flow monitoring
* Abnormal consumption detection
* Possible leakage detection
* Oxygen demand prediction
* Remaining oxygen supply estimation
* Risk classification
* Intelligent alerts
* Hospital monitoring dashboard

## System Workflow

Sensors
   ↓
ESP32
   ↓
Cloud / Backend
   ↓
Database
   ↓
AI Analysis
   ↓
Prediction & Risk Classification
   ↓
Dashboard
   ↓
Alerts

## AI Components

### 1. Anomaly Detection

**Isolation Forest** can be used to identify unusual oxygen consumption patterns.

For example, if the normal oxygen consumption is around 400 L/hour and the system suddenly observes a significantly higher consumption, it can flag the reading as an anomaly.

### 2. Oxygen Demand Prediction

Machine-learning models such as **XGBoost** or **Random Forest** can be used to predict future oxygen demand using historical and real-time consumption data.

### 3. Remaining Supply Estimation

The system can estimate the remaining oxygen duration using the available oxygen and current or predicted consumption rate.

```
Remaining Time = Available Oxygen / Consumption Rate
```

AI-based demand prediction can improve this estimate by considering changing consumption patterns.

## Technologies Used

### Hardware

* ESP32
* Oxygen pressure sensor
* Flow sensor
* Oxygen concentration sensor
* Tank-level sensor

### Software

* Python
* FastAPI
* HTML
* CSS
* JavaScript

### AI / Machine Learning

* Scikit-learn
* Isolation Forest
* XGBoost
* Random Forest
* LSTM (future enhancement)

### Database / Cloud

* Firebase / Supabase

## Project Architecture

Oxygen Sensors
      ↓
    ESP32
      ↓
 Data Transmission
      ↓
Backend / Cloud
      ↓
   Database
      ↓
 AI Processing
 ┌────┴─────────────┐
 ↓                  ↓
Anomaly          Demand
Detection       Prediction
 └────┬─────────────┘
      ↓
Risk Classification
      ↓
Dashboard & Alerts

## Expected Benefits

* Continuous monitoring of oxygen systems
* Earlier identification of abnormal consumption
* Better awareness of possible oxygen shortages
* Improved oxygen supply planning
* Reduced dependence on manual monitoring
* Data-driven decision support for hospital staff

## Project Status

**Prototype / Hackathon Project**

The system is being developed as a prototype to demonstrate real-time oxygen monitoring, AI-based anomaly detection, demand prediction, and intelligent alerting.

## Future Enhancements

* Integration with real hospital oxygen infrastructure
* More accurate prediction using larger real-world datasets
* Advanced time-series models such as LSTM
* Mobile application for alerts
* Integration with hospital management systems
* Automated oxygen refill recommendations

## Team

**Project:** OxyGuard AI
**Domain:** Healthcare + IoT + Artificial Intelligence
**Type:** Hackathon Prototype

## Disclaimer

This project is a prototype for educational and demonstration purposes. It is not intended to replace certified medical or hospital oxygen-management equipment.
