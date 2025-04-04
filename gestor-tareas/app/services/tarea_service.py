from sqlalchemy.orm import Session
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate, TareaUpdate

def obtener_tareas(db: Session):
    return db.query(Tarea).all()

def crear_tarea(db: Session, tarea: TareaCreate):
    nueva_tarea = Tarea(**tarea.dict())
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaUpdate):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        return None
    for key, value in tarea.dict().items():
        setattr(db_tarea, key, value)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def eliminar_tarea(db: Session, tarea_id: int):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if not db_tarea:
        return None
    db.delete(db_tarea)
    db.commit()
    return db_tarea
