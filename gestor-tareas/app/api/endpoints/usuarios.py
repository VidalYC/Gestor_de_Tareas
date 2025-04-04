from fastapi import APIRouter, Security
from app.core.security import obtener_usuario_actual
from app.schemas.usuario import UsuarioResponse
from app.models.usuario import Usuario
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/me", response_model=UsuarioResponse, tags=["Usuarios"])
def leer_usuario_actual(usuario: Usuario = Security(obtener_usuario_actual)):
    logger.debug(f"✅ Usuario autenticado en /me: {usuario.username}")
    return usuario
