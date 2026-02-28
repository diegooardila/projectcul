from fastapi import APIRouter, HTTPException
from controllers.facultad_controller import *
from models.facultad_model import Facultad

router = APIRouter()

nueva_facultad = FacultadController()


@router.post("Crear una Facultad")
async def create_facultad(facultad: Facultad):
    rpta = nueva_facultad.create_facultad(facultad)
    return rpta

@router.get("Obtener una Facultad",response_model=Facultad)
async def get_facultad(id_facultad: int):
    rpta = nueva_facultad.get_facultad(id_facultad)
    return rpta

@router.get("Obtener todas las Facultades")
async def get_facultades():
    rpta = nueva_facultad.get_facultades()
    return rpta