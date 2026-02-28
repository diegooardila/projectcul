from fastapi import APIRouter, HTTPException
from controllers.inscripcion_controller import *
from models.inscripcion_model import Inscripcion

router = APIRouter()

nueva_inscripcion = InscripcionController()


@router.post("Crear una Inscripción")
async def create_inscripcion(inscripcion: Inscripcion):
    rpta = nueva_inscripcion.create_inscripcion(inscripcion)
    return rpta

@router.get("Obtener una Inscripción",response_model=Inscripcion)
async def get_inscripcion(id_inscripcion: int):
    rpta = nueva_inscripcion.get_inscripcion(id_inscripcion)
    return rpta

@router.get("Obtener todas las Inscripciones")
async def get_inscripciones():
    rpta = nueva_inscripcion.get_inscripciones()
    return rpta

@router.put("Actualizar una Inscripción")
async def update_inscripcion(id_inscripcion: int, inscripcion: Inscripcion):
    rpta = nueva_inscripcion.update_inscripcion(id_inscripcion, inscripcion)
    return rpta

@router.delete("Eliminar una Inscripción")
async def delete_inscripcion(id_inscripcion: int):
    rpta = nueva_inscripcion.delete_inscripcion(id_inscripcion)
    return rpta


