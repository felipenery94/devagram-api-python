import time

import jwt
from decouple import config
from Utils.AuthUtil import verificar_senha
from models.UsuarioModel import UsuarioLoginModel
from repositories.UsuarioRepository import buscar_usuario_por_email

JWT_SECRET = config('JWT_SECRET')

def gerar_token_jwt (usuario_id: str) -> str :
    payload = {
        "usuario_id": usuario_id ,
        "tempo_expiração": time.time() + 600

    }
    token = jwt.encode(payload ,  JWT_SECRET ,  algorithm='HS256')

    return token


def decodificar_token_jwt(token:str):
    try:

        token_decodificado = jwt.encode(token , JWT_SECRET ,  algorithm='HS256')

        if token_decodificado["tempo_expiração"] >= time.time():
            return token_decodificado

        else:
            return None


    except Exception as erro:
        print(erro)

        return{
            "mensagem": "Erro interno no servidor",
           "dados":str(erro),
            "status": 500 ,
        }




async def login_service(usuario: UsuarioLoginModel):
    usuario_encontrado = await buscar_usuario_por_email(usuario.email)

    if not  usuario_encontrado:
        return {
            "mensagem": "Email ou senha incorretos",
            "status": 401,
            "dados": ""
        }

    else:
        if verificar_senha(usuario.senha, usuario_encontrado["senha"]):
            return {
                "mensagem": "Login realizado com sucesso",
                "dados": usuario_encontrado,
                "status": 200
            }
        else:
            return {

                "mensagem": "Email ou senha incorretos",
                "status": 401,
                "dados": ""
            }

