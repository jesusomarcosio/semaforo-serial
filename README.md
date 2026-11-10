# Drag Race Tree Controller (Semaforo Serial)

## About The Project
A multi-tier system designed to simulate, read, and manage a drag racing start light tree. The current Python codebase acts as the hardware interface and backend API, responsible for reading real-time data from the physical/simulated race tree box. This data is then broadcasted via a REST API to a dedicated frontend client built in Java.

## Built With
* **Python 3.x** (Hardware Interface & Backend)
* **FastAPI** (API routing and Pydantic data validation)
* **PyMongo** (MongoDB integration for data persistence)
* **PySerial** (Hardware serial port communication)
* **Java** (Frontend GUI)

## Key Features
* **Hardware Integration:** Python modules dedicated to reading and processing serial data from the drag race tree in real-time.
* **Data Bridge:** A robust REST API designed specifically to transmit hardware data to the Java frontend client.
* **Database Management:** MongoDB integration for pilot registration and race time persistence.
* **Port Management:** Built-in utilities for listing active serial ports and safe error handling during hardware disconnection.

## Getting Started

### Prerequisites
* Python 3.8+
* MongoDB running locally or via Atlas
* Java Development Kit (JDK) 11+ (for upcoming frontend features)

### Installation
1. Clone the repo
   ```sh
git clone https://github.com/jesusomarcosio/semaforo-serial.git
