from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, Token
from app.services.usuario_service import crear_usuario, autenticar_usuario, get_usuario_por_username, crear_access_token
from app.core.database import get_db
from app.core.security import obtener_usuario_actual  # Esta función se utiliza para proteger rutas
# Nota: Si deseas usar OAuth2PasswordRequestForm, se podría adaptar para login

router = APIRouter()

@router.post("/register", response_model=UsuarioResponse, tags=["Usuarios"])
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = get_usuario_por_username(db, usuario.username)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crear_usuario(db, usuario)

from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login", response_model=Token, tags=["Usuarios"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = crear_access_token(
        data={"sub": usuario.username}, expires_delta=timedelta(hours=1)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UsuarioResponse, tags=["Usuarios"])
def leer_usuario_actual(usuario=Depends(obtener_usuario_actual)):
    return usuario
