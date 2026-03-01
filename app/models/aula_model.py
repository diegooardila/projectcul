from pydantic import BaseModel

class Aula(BaseModel):
    id_aula: int | None = None
    codigo_aula: str
    capacidad_maxima: int
    id_estado: int