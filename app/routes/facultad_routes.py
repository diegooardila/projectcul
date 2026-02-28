from fastapi import APIRouter, HTTPException
from controllers.facultad_controller import *
from models.facultad_model import Facultad

router = APIRouter()

nueva_facultad = FacultadController()


@router.post("/create_facultad")
async def create_facultad(facultad: Facultad):
    rpta = nueva_facultad.create_facultad(facultad)
    return rpta

@router.get("/get_facultad/{id_facultad}",response_model=Facultad)
async def get_facultad(id_facultad: int):
    rpta = nueva_facultad.get_facultad(id_facultad)
    return rpta

@router.get("/get_facultades")
async def get_facultades():
    rpta = nueva_facultad.get_facultades()
    return rpta