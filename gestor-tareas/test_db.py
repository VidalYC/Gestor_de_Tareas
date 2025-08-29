# test_db.py
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (solo en local)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ No se encontró la variable de entorno DATABASE_URL")

try:
    # Crear motor de la base de datos
    engine = create_engine(DATABASE_URL)

    # Probar conexión
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Conexión exitosa:", result.scalar())

except Exception as e:
    print("❌ Error al conectar con la base de datos:", str(e))
