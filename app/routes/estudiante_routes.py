from fastapi import APIRouter, HTTPException
from controllers.estudiante_controller import *
from models.estudiante_model import Estudiante

router = APIRouter()

nuevo_estudiante = EstudianteController()


@router.post("/create_estudiante/")
async def create_estudiante(estudiante: Estudiante):
    rpta = nuevo_estudiante.create_estudiante(estudiante)
    return rpta


@router.get("/get_estudiante/{id_estudiante}",response_model=Estudiante)
async def get_estudiante(id_estudiante: int):
    rpta = nuevo_estudiante.get_estudiante(id_estudiante)
    return rpta

@router.get("/get_estudiantes")
async def get_estudiantes():
    rpta = nuevo_estudiante.get_estudiantes()
    return rpta

@router.put("/update_estudiante/{id_estudiante}")
async def update_estudiante(id_estudiante: int, estudiante: Estudiante):
    rpta = nuevo_estudiante.update_estudiante(id_estudiante, estudiante)
    return rpta

@router.delete("/delete_estudiante/{id_estudiante}")
async def delete_estudiante(id_estudiante: int):
    rpta = nuevo_estudiante.delete_estudiante(id_estudiante)
    return rpta