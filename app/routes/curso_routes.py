from fastapi import APIRouter, HTTPException
from controllers.curso_controller import *
from models.curso_model import Curso

router = APIRouter()

nuevo_curso = CursoController()


@router.post("/create_curso/")
async def create_curso(curso: Curso):
    rpta = nuevo_curso.create_curso(curso)
    return rpta

@router.get("/get_curso/{id_curso}",response_model=Curso)
async def get_curso(id_curso: int):
    rpta = nuevo_curso.get_curso(id_curso)
    return rpta

@router.get("/get_cursos")
async def get_cursos():
    rpta = nuevo_curso.get_cursos()
    return rpta

@router.put("/update_curso/{id_curso}")
async def update_curso(id_curso: int, curso: Curso):
    rpta = nuevo_curso.update_curso(id_curso, curso)
    return rpta

@router.delete("/delete_curso/{id_curso}")
async def delete_curso(id_curso: int):
    rpta = nuevo_curso.delete_curso(id_curso)
    return rpta


