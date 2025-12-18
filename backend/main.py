from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
from sys import stderr

from backend.modules.calcul import calcul

app = FastAPI()

logger.add(stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("logs/api.log")

logger.debug("L'API est en cours de démarrage...")


@app.get("/")
async def homepage():
    return {"message": "Hello World"}

class CalculInput(BaseModel):
    x: int

@app.post("/calcul")
async def post_calcul(input: CalculInput):
    logger.info(f"Calcul de: {input.x}")
    try:
        return calcul(input.x)
    except Exception as e:        
        logger.error(f"Erreur lors de l'analyse: {e}")        
        return {"error": str(e)}

@app.get('/health')
async def health():
    return { "status": "ok" }