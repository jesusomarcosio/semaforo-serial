from pymongo import MongoClient 
from bson import ObjectId 
from pymongo import DESCENDING
from pymongo.errors import PyMongoError 

# Persistence error exception
class PersistenciaException(Exception):
    pass

cliente = MongoClient("mongodb://localhost:27017") # Create a MongoClient instance 

db = cliente["semaforo"] # Create or acces a database named "semaforo", is already created in prueba_mongo.py

CARRERAS = db.get_collection("carreras") 
PILOTOS = db.get_collection("pilotos") 

# Posts a new race, this method is called in the Endpoint guardar_carrera in api.py
def guardar_carrera(carrera: dict):
    try:
        resultado = CARRERAS.insert_one(carrera) 

        if not resultado.acknowledged:
            raise PersistenciaException(f"Error al guardar la carrera: {e}")
        
        return {"message": f"Carrera guardada correctamente: {resultado.inserted_id}"}
    except PyMongoError as e:
        raise PersistenciaException(f"Error al guardar la carrera: {e}")
    
# Return the last race of the event
def obtener_carrera():
    try: 
        resultado = CARRERAS.find_one(sort=[("_id", DESCENDING)])

        if resultado is None:
            return {"message": "No hay carreras registradas"}
        
        resultado["_id"] = str(resultado["_id"]) 

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
            return {"message": "No hay pilotos registrados"}
        
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
            raise PersistenciaException("No se confirmo la insercion del piloto")
        
        return {"message": f"Piloto guardado correctamente: {resultado.inserted_id}"}
    
    except PyMongoError as e:
        raise PersistenciaException(f"Error al guardar el piloto: {e}")

# Deletes an especific pilot by id
def eliminar_piloto(id: str):
    try:
        id_piloto = ObjectId(id)

        resultado = PILOTOS.delete_one({"_id": id_piloto})

        if resultado.deleted_count == 0:
            return {"message": f"Piloto no encontrado: {id_piloto}"}
        
        return {"message": f"Piloto eliminado correctamente: {id_piloto}"}
    except PyMongoError as e:
        raise PersistenciaException(f"Error al eliminar el piloto: {e}")