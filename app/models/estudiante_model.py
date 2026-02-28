from pydantic import BaseModel

class Estudiante(BaseModel):
    id_estudiante: int | None = None
    codigo_estudiantil: str
    nombres: str
    apellidos: str
    id_usuario: int
    id_facultad: int