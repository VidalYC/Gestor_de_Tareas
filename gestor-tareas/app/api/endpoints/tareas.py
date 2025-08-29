from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import obtener_usuario_actual
from app.models.usuario import Usuario
from app.schemas.tarea import TareaCreate, TareaBase, TareaResponse
from app.services import tarea_service

router = APIRouter(prefix="/tareas", tags=["Tareas"])

@router.post("", response_model=TareaResponse)
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(obtener_usuario_actual)):
    return tarea_service.crear_tarea(db, tarea, usuario.id)

@router.get("", response_model=list[TareaResponse])
def listar_tareas(db: Session = Depends(get_db), usuario: Usuario = Depends(obtener_usuario_actual)):
    return tarea_service.obtener_tareas_por_usuario(db, usuario.id)

@router.get("/{tarea_id}", response_model=TareaResponse)
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(obtener_usuario_actual)):
    tarea = tarea_service.obtener_tarea(db, tarea_id, usuario.id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.put("/{tarea_id}", response_model=TareaResponse)
def actualizar_tarea(tarea_id: int, tarea: TareaBase, db: Session = Depends(get_db), usuario: Usuario = Depends(obtener_usuario_actual)):
    tarea_actualizada = tarea_service.actualizar_tarea(db, tarea_id, tarea, usuario.id)
    if not tarea_actualizada:
        raise HTTPException(status_code=404, detail="No se pudo actualizar la tarea")
    return tarea_actualizada

@router.delete("/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(obtener_usuario_actual)):
    tarea_eliminada = tarea_service.eliminar_tarea(db, tarea_id, usuario.id)
    if not tarea_eliminada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada para eliminar")
