from pydantic import BaseModel , Field ,  EmailStr


class ModelUsuario(BaseModel):
    id : str = Field(...)
    nome: str = Field(...)
    email : EmailStr = Field (...)
    senha : str = Field (...)
    foto : str = Field (...)

    class config:
        schema_extra = {
            "usuario":{
                "nome": "fulano de tal",
                "email": "fulano@gmail.com",
                "senha":"1234abc@",
                "foto": "fulano.png"
            }

        }



class ModelCriarUsuario(BaseModel):
    nome: str = Field(...)
    email : EmailStr = Field (...)
    senha : str = Field (...)
    foto : str = Field (...)

    class config:
        schema_extra = {
            "usuario":{
                "nome": "fulano de tal",
                "email": "fulano@gmail.com",
                "senha":"1234abc@",
                "foto": "fulano.png"
            }

        }



class UsuarioLoginModel(BaseModel):
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class config:
        schema_extra = {
            "usuario": {
                "email": "fulano@gmail.com",
                "senha": "1234abc@"
            }
        }