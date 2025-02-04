from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.messages import router as messages_router
from app.routes.automations import router as automations_router
from app.routes.utils import router as utils_router


app = FastAPI()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1", "http://localhost", "http://IP_DAV_PS"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(messages_router, prefix="/api/messages", tags=["Messages"])
app.include_router(automations_router, prefix="/api/automations", tags=["Automations"])
#Tetes de rotas crewai
app.include_router(utils_router, prefix="/api/utils", tags=["Utils"])


@app.get("/")
def root():
    return {"message": "API está funcionando"}
