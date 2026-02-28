from pydantic import BaseModel

class Facultad(BaseModel):
    id_facultad: int | None = None
    nombre_facultad: str