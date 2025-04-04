from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.tarea import TareaCreate, TareaUpdate, TareaResponse
from app.services.tarea_service import obtener_tareas, crear_tarea, actualizar_tarea, eliminar_tarea

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[TareaResponse])
def listar_tareas(db: Session = Depends(get_db)):
    return obtener_tareas(db)

@router.post("/", response_model=TareaResponse)
def agregar_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crear_tarea(db, tarea)

@router.put("/{tarea_id}", response_model=TareaResponse)
def modificar_tarea(tarea_id: int, tarea: TareaUpdate, db: Session = Depends(get_db)):
    return actualizar_tarea(db, tarea_id, tarea)

@router.delete("/{tarea_id}", response_model=TareaResponse)
def borrar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    return eliminar_tarea(db, tarea_id)
