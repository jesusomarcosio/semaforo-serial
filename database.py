from pymongo import MongoClient # Import the MongoClient class from the pymongo library
from bson import ObjectId # Import ObjectId to convert a String to ObjectId
from pymongo import DESCENDING
from pymongo.errors import PyMongoError # Import PyMongoError to handle mongo erros

cliente = MongoClient("mongodb://localhost:27017") # Create a MongoClient instance 

db = cliente["semaforo"] # Create or acces a database named "semaforo", is already created in prueba_mongo.py

CARRERAS = db.get_collection("carreras") # Get the "carreras" collection from the "semaforo" database
PILOTOS = db.get_collection("pilotos") # Get the "pilotos" collection from the "semaforo" database

# Posts a new race, this method is called in the Endpoint guardar_carrera in api.py
def guardar_carrera(carrera: dict):
    try:
        resultado = CARRERAS.insert_one(carrera) # Insert the carrera document into the carreras collection

        if not resultado.acknowledged:
            raise PersistenciaException("Error al guardar la carrera")
        
        return {f"Carrera guardada correctamente: {resultado.inserted_id}"}# Return the ID of the inserted document
    except PyMongoError as e:
        raise PersistenciaException(f"Error al guardar la carrera: {e}")
    
# Return the last race of the event
def obtener_carrera():
    try: 
        resultado = CARRERAS.find_one(sort=[("_id", DESCENDING)])

        if resultado is None:
            return {"message": "No hay carreras registradas"}
        
        resultado["_id"] = str(resultado["_id"]) # ObjectId to String

        return resultado
    
    except PyMongoError as e:
        raise PersistenciaException(f"Error al obtener la ultima carrera: {e}")

# Return the history of races
def obtener_historial():
    try:
        lista_carreras = list(CARRERAS.find())
        
        for carrera in lista_carreras:
            carrera["_id"] = str(carrera["_id"])

        return lista_carreras

    except PyMongoError as e:
        raise PersistenciaException(f"Error al obtener el historial de carreras: {e}")

# Return the list of pilots
def obtener_pilotos():
    try:
        lista_pilotos = list(PILOTOS.find())

        if len(lista_pilotos) == 0:
            raise PersistenciaException("No hay pilotos registrados")
        
        for piloto in lista_pilotos:
            piloto["_id"] = str(piloto["_id"])

        return lista_pilotos
    
    except PyMongoError as e:
        raise PersistenciaException(f"Error al obtener la lista de pilotos: {e}")

# Store a new pilot
def guardar_piloto(piloto: dict):
    try:
        resultado = PILOTOS.insert_one(piloto)

        if not resultado.acknowledged:
            raise PyMongoError("Error al guardar el piloto")
        
        return {f"Piloto guardado correctamente: {resultado.inserted_id}"}
    
    except PyMongoError as e:
        raise PersistenciaException(f"Error al guardar el piloto: {e}")

# Deletes an especific pilot by id
def eliminar_piloto(id: str):
    id_piloto = ObjectId(id)

    resultado = PILOTOS.delete_one({"_id": id_piloto})

    if resultado.deleted_count == 0:
        raise PersistenciaException("Piloto no encontrado")
    
    return {"message": f"Piloto eliminado correctamente: {id_piloto}"}

# Persistence error exception
class PersistenciaException(Exception):
    pass