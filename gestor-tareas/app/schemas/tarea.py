from pydantic import BaseModel

class TareaBase(BaseModel):
    titulo: str
    descripcion: str

class TareaCreate(TareaBase):
    pass

class TareaUpdate(TareaBase):
    completado: bool

class TareaResponse(TareaBase):
    id: int
    completado: bool

    class Config:
        orm_mode = True
