from fastapi import FastAPI
import django
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()
@app.get("/")
async def root():
        return templates.TemplateResponse("main.html", {'request': request})

