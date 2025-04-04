from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioLogin, Token
from app.services import usuario_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UsuarioResponse)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    
    db_usuario = usuario_service.get_usuario_por_username(db, usuario.username)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return usuario_service.crear_usuario(db, usuario)

@router.post("/login", response_model=Token)
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    db_usuario = usuario_service.autenticar_usuario(db, usuario.username, usuario.password)
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = usuario_service.crear_access_token(data={"sub": db_usuario.username})
    return {"access_token": access_token, "token_type": "bearer"}
