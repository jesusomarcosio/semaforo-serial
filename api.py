from fastapi import FastAPI, HTTPException
import database
from database import PersistenciaException
from pydantic import BaseModel

class Piloto(BaseModel):
    nombre: str
    equipo: str
    categoria: str

class Carrera(BaseModel):
    RT: float
    sixty_ft: float
    ET: float
    MPH: float

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
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to post the data of a new race
@app.post("/carrera")
def guardar_carrera(carrera: Carrera):
    try:
        return database.guardar_carrera(carrera.model_dump())
    except PersistenciaException as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get the history of all races
@app.get("/carreras")
def obtener_historial():
    try:
        return database.obtener_historial()
    except PersistenciaException as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get the list of pilots
@app.get("/pilotos")
def obtener_pilotos():
    try:
        return database.obtener_pilotos()
    except PersistenciaException as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to post a new pilot 
@app.post("/piloto")
def guardar_piloto(piloto: Piloto):
    try:
        return database.guardar_piloto(piloto.model_dump())
    except PersistenciaException as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to delete a pilot
@app.delete("/piloto/{id}")
def eliminar_piloto(id: str):
    try:
        return database.eliminar_piloto(id)
    except PersistenciaException as e:
        raise HTTPException(status_code=500, detail=str(e))
