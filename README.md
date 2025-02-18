# Integrated Accident Detection and Monitoring System

## Overview
The **Integrated Accident Detection and Monitoring System** is a comprehensive solution designed to detect accidents in real-time, monitor the situation, and relay critical information to relevant parties. The system consists of:
- A **Django server** acting as the web API.
- An **ESP32 microcontroller** for hardware data collection and communication.
- A **webcam** for capturing image data, which is processed by a machine learning model hosted on the Django server.
- **Third-party application integration** for disseminating accumulated information.

This system is ideal for applications in traffic management, anomaly detection, emergency response, and vehicle safety.

---

## Features
1. **Real-Time Data Collection**:
   - Collects sensor data (e.g., accelerometer, GPS) from the ESP32 microcontroller.
   - Captures image data from a webcam for accident detection.

2. **Accident and Anomaly Detection**:
   - Processes image data using a machine learning model hosted on the Django server.
   - Analyzes sensor data to detect anomalies indicative of accidents.

3. **Data Communication**:
   - Sends and receives data to/from the ESP32 microcontroller via a dedicated API endpoint.
   - Relays processed information to third-party applications (e.g., emergency services, traffic management systems).

4. **Scalable Web API**:
   - Built using Django, providing a robust and scalable backend for data handling and processing.

---

## System Architecture
The system is divided into three main components:
1. **Hardware (ESP32 Microcontroller)**:
   - Collects sensor data (e.g., acceleration, location).
   - Communicates with the Django server via HTTP requests.

2. **Django Server**:
   - Hosts the web API with multiple endpoints for data collection, processing, and dissemination.
   - Runs a machine learning model for image-based accident detection.

3. **Third-Party Applications**:
   - Receive processed data from the Django server for further action (e.g., emergency alerts, traffic updates).

---

## API Endpoints
The Django server provides the following endpoints:

### 1. **ESP32 Data Endpoint**
- **URL**: `/upload/`
- **Method**: `POST`
- **Description**: Receives sensor data from the ESP32 microcontroller.
- **Request Body**:
  ```json
  {
    "acceleration": [x, y, z],
    "location": {"latitude": 0.0, "longitude": 0.0},
    "timestamp": "2023-10-01T12:00:00Z"
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "message": "Data received"
  }
  ```

### 2. **Webcam Image Endpoint**
- **URL**: `/camera/`
- **Method**: `POST`
- **Description**: Receives image data from a webcam for accident detection.
- **Request Body**:
  ```json
  {
    "image": "base64_encoded_image_data",
    "timestamp": "2023-10-01T12:00:00Z"
  }
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "accident_detected": true,
    "confidence": 0.95
  }
  ```

### 3. **Third-Party Data Endpoint**
- **URL**: `/ret/len=<int:pk>/`, `ret/region=<str:pk>/`
- **Method**: `GET`
- **Description**: Provides accumulated accident data to third-party applications.
- **Response**:
  ```json
  {
    "accidents": [
      {
        "location": {"latitude": 0.0, "longitude": 0.0},
        "timestamp": "2023-10-01T12:00:00Z",
        "severity": "high"
      }
    ]
  }
  ```

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 4.0+
- ESP32 microcontroller with HTTP capabilities
- Webcam for image capture
- Machine learning model for accident detection

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/accident-detection-system.git
   cd accident-detection-system
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Django Server**:
   ```bash
   python manage.py runserver
   ```

6. **Configure the ESP32**:
   - Update the ESP32 code with the Django server's IP address and API endpoint.
   - Ensure the ESP32 can send HTTP POST requests to `/upload`.

7. **Set Up the Webcam**:
   - Ensure the webcam is connected and can send image data to `/camera/`.

---

## Usage
1. **Start the System**:
   - Power on the ESP32 microcontroller and webcam.
   - Start the Django server.

2. **Monitor Data**:
   - Use the Django admin panel or third-party applications to monitor incoming data and accident alerts.

3. **Test Endpoints**:
   - Use tools like **Postman**, **Restfox** or **cURL** to test the API endpoints.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Thanks to the Django community for providing an excellent web framework.
- Special thanks to the developers of the ESP32 and machine learning libraries used in this project.

---

## Contact
For questions or feedback, please contact:
- **Okereke Vincent Princewill**  
- **Email**: vincentprincewill44@gmail.com  
- **GitHub**: [CrimsonKarma44](https://github.com/CrimsonKarma44)

---
