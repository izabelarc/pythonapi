from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from apiTools import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/saudacao")
async def get():
    return{"msg": "olá mundo!"}