from pydantic import BaseModel
from datetime import datetime

class Inscripcion(BaseModel):
    id_inscripcion: int | None = None
    id_estudiante: int
    id_curso: int
    fecha_registro: datetime
    id_estado: int