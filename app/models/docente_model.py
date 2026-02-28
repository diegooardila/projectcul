from pydantic import BaseModel

class Docente(BaseModel):
    id_docente: int | None = None
    numero_documento: str
    nombres: str
    apellidos: str
    id_usuario: int
    id_facultad: int