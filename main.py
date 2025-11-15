from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


app = FastAPI()


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
