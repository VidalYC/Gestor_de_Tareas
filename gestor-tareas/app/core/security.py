import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.usuario_service import get_usuario_por_username
from dotenv import load_dotenv

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login") 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definida en las variables de entorno.")

def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Mensajes de depuración:
    print(f"🔹 Token recibido: {token}")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"✅ Payload decodificado: {payload}")
        username: str = payload.get("sub")
        if username is None:
            print("⚠️ El token no contiene 'sub'")
            raise credentials_exception
    except JWTError as e:
        print(f"❌ Error al decodificar el token: {e}")
        raise credentials_exception

    usuario = get_usuario_por_username(db, username)
    if usuario is None:
        print(f"⚠️ Usuario '{username}' no encontrado en la base de datos.")
        raise credentials_exception

    print(f"✅ Usuario autenticado: {usuario.username}")
    return usuario
