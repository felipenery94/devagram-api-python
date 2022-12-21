from fastapi import APIRouter, Body, HTTPException
from Service.AuthService import login_service, gerar_token_jwt
from models.UsuarioModel import UsuarioLoginModel

router = APIRouter()



@router.post('/login')

async def login (usuario: UsuarioLoginModel = Body(...)):

    resultado = await login_service(usuario)

    if not resultado ["status"] == 200:
        raise HTTPException (status_code= resultado ["status"] ,  detail= resultado["mensagem"])

    del resultado ["dados"]["senha"]

    token =  gerar_token_jwt(resultado ["dados"]["id"])
    resultado['token'] = token

    return resultado

