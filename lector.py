import serial # import pyserial library to handle serial communication

# Opens a connection to the serial port
puerto = serial.Serial('/dev/pts/5', 9600) # '/dev/pts/5' is the port direction and 9600 is the baud rate

print("Esperando datos de la caja...")

try:
    while True:
        # Verifys if there is data waiting to be read from the port
        if puerto.in_waiting > 0: 
            try:
                # Reads a data line from de port, decodes it form bytes to string and removes any leading/trailing whitespace
                datos = puerto.readline().decode().strip() 

                print(f"Recibido: {datos}")
                
                # Dictionary where the race data will be stored as key-value pairs
                carrera = {}
                # Splits the data string into parts and processes each part to extract key-value pairs
                partes = datos.split(',')
                for parte in partes:
                    clave, valor = parte.split(':')
                    carrera[clave] = float(valor)

                    if clave == "RT":
                        tiempo_reaccion = float(valor)
                    elif clave == "MPH":
                        velocidad = float(valor)
                
                # Print the race data
                print(f"Tiempo de reaccion: {carrera['RT']}s")
                print(f"Tiempo a los 60 pies: {carrera['60FT']}s")
                print(f"Tiempo final: {carrera['ET']}s")
                print(f"Velocidad: {carrera['MPH']} mph")

                # Evaluates the reaction time and provides feedback based on the reaction time
                if tiempo_reaccion < 0.500:
                    print("¡Buen tiempo de reacción!")
                else:
                    print("Tiempo de reacción lento")

                # Evaluates the speed and provides feedback based on the speed
                if velocidad > 150.0:
                    print("¡Carrera rápida!")
                elif velocidad >= 120.0:
                    print("Velocidad normal")
                else:
                    print("Carrera lenta")
            # Handles potential while processing the data or converting strings to floats
            except ValueError:
                print(f"Datos erroneos: {datos}")
            # Handles any other exceptions that may occur during data processing
            except Exception as e:
                print(f"Error al procesar los datos: {e}")

            # Add a separator for better readability of the output
            print("---")
finally:
    # Closes the port connection when the program is stopped
    puerto.close()
    print("Puerto cerrado correctamente.")