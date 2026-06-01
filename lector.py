import serial #importa la libreria pyserial para comunicarse con el puerto serial

# Abre una conexion al puerto serial 
puerto = serial.Serial('/dev/pts/5', 9600) # '/dev/pts/5' es la direccion del puerto y 9600 es la velocidad de comunicacion

print("Esperando datos de la caja...")

while True:
    # Verifica si hay datos disponibles para leer en el puerto
    if puerto.in_waiting > 0: 
        # Lee una linea de datos del puerto, decodifica de bytes a string y elimina espacios en blanco
        datos = puerto.readline().decode().strip() 

        print(f"Recibido: {datos}")
        
        # Separar los datos
        partes = datos.split(',')
        for parte in partes:
            clave, valor = parte.split(':')

            print(f"{clave}: {valor}")

            if clave == "RT":
                tiempo_reaccion = float(valor)
            elif clave == "MPH":
                velocidad = float(valor)
        
        if tiempo_reaccion < 0.500:
            print("¡Buen tiempo de reacción!")
        else:
            print("Tiempo de reacción lento")

        if velocidad > 150.0:
            print("¡Carrera rápida!")
        elif velocidad >= 120.0:
            print("Velocidad normal")
        else:
            print("Carrera lenta")
   
        # Agrega una linea para separar cada lectura de datos
        print("---")