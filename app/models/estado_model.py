from pydantic import BaseModel

class Estado(BaseModel):
    id_estado: int | None = None
    nombre_estado: str