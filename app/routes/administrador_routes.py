from fastapi import APIRouter, HTTPException
from controllers.administrador_controller import *
from models.administrador_model import Administrador

router = APIRouter()

nuevo_administrador = AdministradorController()


@router.post("/create_administrador/")
async def create_administrador(administrador: Administrador):
    rpta = nuevo_administrador.create_administrador(administrador)
    return rpta


@router.get("/get_administrador/{id_administrador}",response_model=Administrador)
async def get_administrador(id_administrador: int):
    rpta = nuevo_administrador.get_administrador(id_administrador)
    return rpta

@router.get("/get_administradores")

async def get_administradores():
    rpta = nuevo_administrador.get_administradores()
    return rpta