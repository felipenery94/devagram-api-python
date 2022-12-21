from fastapi import APIRouter, Body, HTTPException
from models.UsuarioModel import ModelCriarUsuario
from repositories.UsuarioRepository import criar_usuario

router = APIRouter()


@router.post("/", response_description="Rota para criar novos usuários")
async def rota_criar_usuario(usuario:ModelCriarUsuario = Body(...)):
    resultado = await criar_usuario(usuario)

    try:
        if not resultado ==201:
            raise HTTPException (status_code= resultado["status"], detail = resultado["mensagem"])


        return resultado
    except Exception as erro:
        print(erro)

        return {
            "Erro interno no servidor"
        }