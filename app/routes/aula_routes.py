from fastapi import APIRouter, HTTPException
from controllers.aula_controller import *
from models.aula_model import Aula

router = APIRouter()

nueva_aula = AulaController()


@router.post("/create_aula/")
async def create_aula(aula: Aula):
    rpta = nueva_aula.create_aula(aula)
    return rpta


@router.get("/get_aula/{id_aula}",response_model=Aula)
async def get_aula(id_aula: int):
    rpta = nueva_aula.get_aula(id_aula)
    return rpta

@router.get("/get_aulas")

async def get_aulas():
    rpta = nueva_aula.get_aulas()
    return rpta