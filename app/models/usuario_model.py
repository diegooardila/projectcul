from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: int = None
    correo_electronico: str
    contrasena_hash: str
    rol: str
    id_estado: int