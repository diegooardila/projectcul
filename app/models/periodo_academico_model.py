from pydantic import BaseModel
from datetime import date

class PeriodoAcademico(BaseModel):
    id_periodo: int | None = None
    codigo_periodo: str
    fecha_inicio: date
    fecha_fin: date