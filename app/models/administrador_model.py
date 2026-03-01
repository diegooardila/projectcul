from pydantic import BaseModel

class Administrador(BaseModel):
    id_administrador: int | None = None
    numero_documento: str
    nombres: str
    apellidos: str
    id_usuario: int