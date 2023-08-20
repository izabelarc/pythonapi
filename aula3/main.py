from fastapi import FastAPI, Depends
from data import cursos
from apiTols import fake_db
from typing import Any

app = FastAPI()

@app.get("/cursos")
async def get(db: Any = Depends(fake_db)):
    return cursos