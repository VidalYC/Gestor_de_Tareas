import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (en local)
load_dotenv()

# Obtiene la URL de la base de datos desde variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ No se encontró la variable de entorno DATABASE_URL")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
