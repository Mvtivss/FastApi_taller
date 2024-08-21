import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URI de MongoDB desde las variables de entorno
MONGODB_URI = os.getenv("MONGODB_URI")

# Conexión a MongoDB
client = MongoClient(MONGODB_URI)
db = client["mydatabase"]