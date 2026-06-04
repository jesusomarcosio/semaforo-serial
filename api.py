from fastapi import FastAPI
import database
from database import PersistenciaException

# Create a FastAPI instance
app = FastAPI()     

# Welcome endpoint to verify that the API is running
@app.get("/")
def inicio():
    return {"message": "Bienvenido a la API de carreras de drag!"}

# Endpoint to get the data of the last race
@app.get("/carrera")
def obtener_carrera():
    try: 
        return database.obtener_carrera()
    except PersistenciaException as e:
        return {"error": str(e)}

# Endpoint to post the data of a new race
@app.post("/carrera")
def guardar_carrera(carrera: dict):
    try:
        return database.guardar_carrera(carrera)
    except PersistenciaException as e:
        return {"error": str(e)}

# Endpoint to get the history of all races
@app.get("/carreras")
def obtener_historial():
    try:
        return database.obtener_historial()
    except PersistenciaException as e:
        return {"error": str(e)}

# Endpoint to get the list of pilots
@app.get("/pilotos")
def obtener_pilotos():
    try:
        return database.obtener_pilotos()
    except PersistenciaException as e:
        return {"error": str(e)}

# Enpoint to post a new pilot 
@app.post("/piloto")
def guardar_piloto(piloto: dict):
    try:
        return database.guardar_piloto(piloto)
    except PersistenciaException as e:
        return {"error": str(e)}

# Endpoint to delete a pilot
@app.delete("/piloto/{id}")
def eliminar_piloto(id: str):
    try:
        return database.eliminar_piloto(id)
    except PersistenciaException as e:
        return {"error": str(e)}
