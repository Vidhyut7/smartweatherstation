# smartweatherstation

This project is a smart, low-cost, and efficient weather monitoring system developed using IoT technologies. The system is capable of measuring temperature, humidity, atmospheric pressure, and altitude in real time. It also features a web interface to display sensor data, built with a FastAPI backend and a MySQL database.

## Project Objective

To build an IoT system that:
- Accurately measures environmental parameters
- Operates with low memory and power consumption
- Offers real-time data monitoring
- Is cost-effective and robust in performance

## Features

- Real-time data collection every 10 seconds from sensors
- Sensor readings include:
  - Temperature (°C)
  - Humidity (%)
  - Pressure (hPa)
  - Altitude (m)
- Wi-Fi-based data transmission
- FastAPI-based backend to receive and serve data
- MySQL database to store sensor logs
- Web dashboard for live monitoring built with HTML, CSS, and JavaScript

## Technologies Used

- **ESP32 Microcontroller**
- **DHT11 Sensor** (Temperature and Humidity)
- **BMP280 Sensor** (Pressure and Altitude)
- **Arduino IDE** for firmware development
- **FastAPI** for backend API
- **MySQL** for data storage
- **HTML, CSS, JavaScript** for frontend interface

## System Architecture

1. **ESP32** reads data from DHT11 and BMP280 sensors.
2. Sends JSON-formatted data to the FastAPI server over Wi-Fi.
3. FastAPI stores the data in a MySQL database.
4. Frontend web dashboard retrieves and displays the latest sensor data.

## Project Workflow

1. Connect ESP32 with DHT11 and BMP280.
2. Upload Arduino code to ESP32 to:
   - Connect to Wi-Fi
   - Collect and send data periodically
3. Set up FastAPI server to handle POST requests and connect to MySQL.
4. Build web dashboard to show live sensor data.
5. Test the entire system under various conditions.

## Key Performance Indicators (KPIs)

- **Sensor Accuracy**: Compare with calibrated equipment
- **Data Transmission Rate**: Monitor API success rate
- **Database Performance**: Measure response time under load
- **Power Consumption**: Evaluate ESP32 energy efficiency
- **Storage Utilization**: Monitor database size over time

## Milestones

- Hardware setup and ESP32 programming
- Backend server with FastAPI and MySQL integration
- Frontend dashboard development
- End-to-end system testing and optimization

## Constraints

- Must meet low power and memory requirements
- Built within a limited budget
- Reliable performance under varying environmental conditions
- Developed within an 8-week internship duration

## Future Improvements

- Add more sensors (e.g., rain, UV index)
- Implement alert notifications for extreme values
- Add user authentication to the web dashboard
- Introduce predictive weather analytics

## Author

**S. Vidhyut**  
B.Tech in Electronics & Communication Engineering  
SRM Institute of Science and Technology  
Intern at FocusR Technology and Consultancy Services  
Sept–Oct 2024

## License

This project is for academic and learning purposes only.
