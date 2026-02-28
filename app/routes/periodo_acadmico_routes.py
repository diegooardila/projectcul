from fastapi import APIRouter, HTTPException
from controllers.periodo_academico_controller import *
from models.periodo_academico_model import PeriodoAcademico

router = APIRouter()

nuevo_periodoAcademico = PeriodoAcademicoController()


@router.post("Crear un Periodo Académico")
async def create_periodo_academico(periodo_academico: PeriodoAcademico):
    rpta = nuevo_periodoAcademico.create_periodo_academico(periodo_academico)
    return rpta


@router.get("Obtener un Periodo Académico",response_model=PeriodoAcademico)
async def get_periodo_academico(id_periodo: int):
    rpta = nuevo_periodoAcademico.get_periodo_academico(id_periodo)
    return rpta

@router.get("Obtener todos los Periodos Académicos")
async def get_periodos_academicos():
    rpta = nuevo_periodoAcademico.get_periodos_academicos()
    return rpta