import os
import logging
from fastapi import Depends, HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.usuario_service import get_usuario_por_username

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Usamos HTTPBearer para extraer el token del header Authorization
bearer_scheme = HTTPBearer()

# Configuración para JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definida en las variables de entorno. Asegúrate de configurarla correctamente.")

def get_db():
    """Obtiene la sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def obtener_usuario_actual(
    credentials: HTTPAuthorizationCredentials = Security(bearer_scheme),
    db: Session = Depends(get_db)
):
    """Obtiene el usuario autenticado a partir del token JWT extraído mediante HTTPBearer"""
    
    token = credentials.credentials
    logger.debug(f"🔹 Token recibido: {token}")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se proporcionó un token de autenticación",
            headers={"WWW-Authenticate": "Bearer"},
        )

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.debug(f"✅ Token decodificado correctamente: {payload}")

        username: str = payload.get("sub")
        if username is None:
            logger.debug("⚠️ El token no contiene 'sub'")
            raise credentials_exception

    except JWTError as e:
        logger.debug(f"❌ Error al decodificar el token: {e}")
        raise credentials_exception

    # Buscar usuario en la base de datos
    usuario = get_usuario_por_username(db, username)
    if usuario is None:
        logger.debug(f"⚠️ Usuario '{username}' no encontrado en la base de datos.")
        raise credentials_exception

    logger.debug(f"✅ Usuario autenticado: {usuario.username}")
    return usuario
