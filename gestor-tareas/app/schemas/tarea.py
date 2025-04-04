from pydantic import BaseModel
from datetime import datetime

class TareaBase(BaseModel):
    titulo: str
    descripcion: str | None = None
    estado: str = "pendiente"  # o usar un Enum si lo prefieres
    prioridad: str = "media"
    fecha_limite: datetime | None = None

class TareaCreate(TareaBase):
    pass

class TareaResponse(TareaBase):
    id: int
    usuario_id: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True
