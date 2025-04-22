from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.cotizaciones import obtener_cotizaciones
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    cotizaciones = obtener_cotizaciones()
    return templates.TemplateResponse("index.html", {"request": request, "cotizaciones": cotizaciones})