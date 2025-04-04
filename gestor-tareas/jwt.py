from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables del .env
SECRET_KEY = os.getenv("SECRET_KEY")

print(f"🔑 SECRET_KEY cargada: {SECRET_KEY}")  # Depuración
