from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()     

# List to store the history of races
historial_carreras = []

# List to store the data of the pilots, which can be expanded in the future to include more details about the pilots
pilotos = []

# Variable to store the data of the last race
ultima_carrera = {
    "RT": 0.0,
    "60FT": 0.0,
    "ET": 0.0,
    "MPH": 0.0
}

# Welcome endpoint to verify that the API is running
@app.get("/")
def inicio():
    return {"message": "Bienvenido a la API de carreras de drag!"}

# Endpoint to get the data of the last race
@app.get("/carrera")
def obtener_carrera():
    return ultima_carrera

# Endpoint to post the data of a new race
@app.post("/carrera")
def guardar_carrera(carrera: dict):
    historial_carreras.append(carrera) 
    return {"message": "Carrera guardada", "total_carreras": len(historial_carreras)}

# Endpoint to get the history of all races
@app.get("/carreras")
def obtener_historial():
    return historial_carreras

# Endpoint to get the list of pilots
@app.get("/pilotos")
def obtener_pilotos():
    if not pilotos:
        return {"message": " No hay pilotos registrados"}
    return pilotos

# Enpoint to post a new pilot 
@app.post("/piloto")
def guardar_piloto(piloto: dict):
    pilotos.append(piloto)
    return {"message": "piloto guardado", "total_pilotos": len(pilotos)}

# Endpoint to get a especific pilot by index
@app.get("/piloto/{index}")
def obtener_piloto(index: int):
    # Validates the index avoiding to search a pilot that doesnt exist in the list
    if index < 0 or index >= len(pilotos):
        return {"message": "Piloto no encontrado"}
    return pilotos[index]

# Endpoint to delete a specific pilot by index
@app.delete("/piloto/{index}")
def eliminar_piloto(index: int):
    if index < 0 or index >= len(pilotos):
        return {"message": "Piloto no encontrado"}
    pilotos.pop(index)
    return {"message": "Piloto eliminado", "total_pilotos": len(pilotos)}
