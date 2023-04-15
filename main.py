from fastapi import FastAPI
from data.Sedes import sedes
from data.Himnos import himnos
from data.Himnarios import himnarios

app = FastAPI()

@app.get("/")
def index():
    return "index"

# @app.get("/membresia")
# def listar_miembros():
#     usuarios = pd.read_csv("./data/membresia.csv")
#     return json.loads(usuarios.to_json(orient='records'))

@app.get("/sedes")
def listar_sedes():
    return sedes

@app.get("/himnos")
def listar_himnos():
    return himnos

@app.get("/himnarios")
def listar_himnarios():
    return himnarios