from sqlalchemy.orm import Session
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate, TareaBase

def crear_tarea(db: Session, tarea: TareaCreate, usuario_id: int) -> Tarea:
    nueva_tarea = Tarea(**tarea.dict(), usuario_id=usuario_id)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def obtener_tareas_por_usuario(db: Session, usuario_id: int):
    return db.query(Tarea).filter(Tarea.usuario_id == usuario_id).all()

def obtener_tarea(db: Session, tarea_id: int, usuario_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.usuario_id == usuario_id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaBase, usuario_id: int):
    db_tarea = obtener_tarea(db, tarea_id, usuario_id)
    if db_tarea:
        for key, value in tarea.dict().items():
            setattr(db_tarea, key, value)
        db.commit()
        db.refresh(db_tarea)
    return db_tarea

def eliminar_tarea(db: Session, tarea_id: int, usuario_id: int):
    db_tarea = obtener_tarea(db, tarea_id, usuario_id)
    if db_tarea:
        db.delete(db_tarea)
        db.commit()
    return db_tarea
