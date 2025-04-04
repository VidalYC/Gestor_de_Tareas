from fastapi import FastAPI
from app.api.endpoints import tareas, auth #, usuarios
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(tareas.router, prefix="/tareas", tags=["Tareas"])
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
#app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])

@app.get("/")
def home():
    return {"message": "Gestor de Tareas API"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Gestor de Tareas API",
        version="1.0.0",
        description="API para gestión de tareas",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

