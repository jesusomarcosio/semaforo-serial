import serial # import pyserial library to handle serial communication
import time # import time library to handle pauses between data transmissions
import random # import random library to generate random data for simulation

# Opens de port connection where is going to write the simulated data, and is going to be read by lector.py
puerto = serial.Serial('/dev/pts/4', 9600)

def simular_caja():
    try:
        while True:
            # sends a invalid data 1 out of 4 times to test error handling in lector.py
            if random.randint(1, 4) == 1:
                datos = "DATO_CORRUPTO_XYZ\n"
            else:
                tiempo_reaccion = round(random.uniform(0.001, 0.999), 3)
                tiempo_60pies = round(random.uniform(0.800, 1.200), 3)
                tiempo_final = round(random.uniform(8.000, 15.000), 3)
                velocidad = round(random.uniform(100.0, 200.0), 2)
                datos = f"RT:{tiempo_reaccion},60FT:{tiempo_60pies},ET:{tiempo_final},MPH:{velocidad}\n"

            # wirtes the simulated data to the port, which will be read by lector.py 
            puerto.write(datos.encode()) # encodes the string data to bytes before sending it through the serial port

            # prints the sent data to the console for verification
            print(f"Enviado: {datos}")

            # 2 second pause before sending the next data, like simulating the time between races
            time.sleep(2)
    finally:
        # Closes the port connection when the simulation is stopped
        puerto.close()
        print("Puerto cerrado correctamente.")

simular_caja()