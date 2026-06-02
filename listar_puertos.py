import serial.tools.list_ports # import list_ports from pyserial to list available serial ports

puertos = serial.tools.list_ports.comports() # get a list of available serial ports

#  Filter the list of ports to include only those that are likely to be USB serial devices (like Arduino or similar)
puertos_usb = [p for p in puertos if "USB" in p.device or "ACM" in p.device]

if not puertos_usb:
    print("No se encontraron puertos seriales disponibles.")
else:
    print("Puertos seriales disponibles:")
    for puerto in puertos_usb:
        print(f"{puerto.device} - {puerto.description}") # print the port device and description