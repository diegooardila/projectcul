from fastapi import APIRouter, HTTPException
from controllers.usuario_controller import *
from models.usuario_model import Usuario

router = APIRouter()

nuevo_usuario = UsuarioController()


@router.post("Crear un Usuario")
async def create_usuario(usuario: Usuario):
    rpta = nuevo_usuario.create_usuario(usuario)
    return rpta


@router.get("Obtener un Usuario",response_model=Usuario)
async def get_usuario(id_usuario: int):
    rpta = nuevo_usuario.get_usuario(id_usuario)
    return rpta

@router.get("Obtner todos los usuarios")
async def get_usuarios():
    rpta = nuevo_usuario.get_usuarios()
    return rpta