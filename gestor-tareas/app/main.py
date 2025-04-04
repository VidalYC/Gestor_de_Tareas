from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import usuarios, tareas

app = FastAPI(title="Gestor de Tareas API")

# Configuración de CORS
origins = [
    "http://localhost:8082"  # Cambia esta URL al dominio de tu frontend si es diferente
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas principales
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(tareas.router, tags=["Tareas"])

@app.get("/")
def home():
    return {"message": "Bienvenido al Gestor de Tareas API"}
