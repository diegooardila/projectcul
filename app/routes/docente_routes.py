from fastapi import APIRouter, HTTPException
from controllers.docente_controller import *
from models.docente_model import Docente

router = APIRouter()

nuevo_docente = DocenteController()


@router.post("/create_docente/")
async def create_docente(docente: Docente):
    rpta = nuevo_docente.create_docente(docente)
    return rpta


@router.get("/get_docente/{id_docente}",response_model=Docente)
async def get_docente(id_docente: int):
    rpta = nuevo_docente.get_docente(id_docente)
    return rpta

@router.get("/get_docentes")
async def get_docentes():
    rpta = nuevo_docente.get_docentes()
    return rpta