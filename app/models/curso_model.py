from pydantic import BaseModel

class Curso(BaseModel):
    id_curso: int | None = None
    codigo_curso: str
    nombre_curso: str
    cupo_maximo: int
    fecha_hora: str
    id_docente: int
    id_aula: int
    id_periodo: int
    id_estado: int