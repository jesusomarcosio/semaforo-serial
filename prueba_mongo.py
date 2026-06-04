from pymongo import MongoClient # Import MongoClient to connect to MongoDB

cliente = MongoClient("mongodb://localhost:27017") # Connect to MongoDB server running on localhost at port 27017

db = cliente["semaforo"] # Create a database named "semaforo"

carreras = db["carreras"] # Create a collection named "carreras"

carrera = {
    "RT": 0.450,
    "60FT": 0.950,
    "ET": 9.500,
    "MPH": 145.50
}

resultado = carreras.insert_one(carrera) # Insert the carrera document into the carreras collection

print(f"Carrera guardada con  ID: {resultado.inserted_id}") # Print the ID of the inserted document

for c in carreras.find():
    print(c) # Print all documents in the carreras collection
