from fastapi import FastAPI
from app.api.endpoints import usuarios, tareas

app = FastAPI(title="Gestor de Tareas API")

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(tareas.router, prefix="/tareas", tags=["Tareas"])

@app.get("/")
def home():
    return {"message": "Bienvenido al Gestor de Tareas API"}
