from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import os

# Contexto para hashear contraseñas con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Obtén la SECRET_KEY desde las variables de entorno o usa un valor por defecto (solo para pruebas)
SECRET_KEY = os.getenv("SECRET_KEY", "MI_CLAVE_SECRETA")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 1

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def crear_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:
    hashed_password = get_password_hash(usuario.password)
    db_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        hashed_password=hashed_password
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario_por_username(db: Session, username: str) -> Usuario:
    return db.query(Usuario).filter(Usuario.username == username).first()

def autenticar_usuario(db: Session, username: str, password: str) -> Usuario:
    usuario = get_usuario_por_username(db, username)
    if not usuario:
        return None
    if not pwd_context.verify(password, usuario.hashed_password):
        return None
    return usuario

def crear_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Genera un token JWT que incluye la información pasada en 'data'.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
