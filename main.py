#Como retornar arquivos no FastAPI
#
from Festapi import FastAPI
from fastapi.responses import FileResponse
from festapi.responses import TemplateResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/curriculo")
def curriculo():
    return FileResponse('files/curriculo')


@app.get("/templates")
def templates():
    return FileResponse('files/index.html')


@app.get("/templates")
def templates():
    return TemplateResponse('templates/index.html')    