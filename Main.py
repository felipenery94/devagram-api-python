from fastapi import FastAPI
from routes.UsuarioRout import router as UsuarioRout

from routes.AutentificacaoRoute import  router as AutentificacaoRoute

app = FastAPI()

app.include_router(UsuarioRout,  tags = ["usuario"] ,  prefix="/api/usuario")

app.include_router(AutentificacaoRoute ,  tags=["Autentificação"] , prefix="/api/auth")



@app.get("/api/health" , tags=["health"])
async def health():
    return{
        "status": "ok"
    }
