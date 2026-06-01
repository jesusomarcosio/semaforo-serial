import serial
import time
import random

# Escribe datos al puerto virtual
puerto = serial.Serial('/dev/pts/4', 9600)

def simular_caja():
    while True:
        tiempo_reaccion = round(random.uniform(0.001, 0.999), 3)
        tiempo_60pies = round(random.uniform(0.800, 1.200), 3)
        tiempo_final = round(random.uniform(8.000, 15.000), 3)
        velocidad = round(random.uniform(100.0, 200.0), 2)
        
        datos = f"RT:{tiempo_reaccion},60FT:{tiempo_60pies},ET:{tiempo_final},MPH:{velocidad}\n"
        puerto.write(datos.encode())
        print(f"Enviado: {datos}")
        time.sleep(2)

simular_caja()