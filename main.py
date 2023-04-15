from fastapi import FastAPI
from data.Sedes import sedes
from data.HimnarioNegro import himnarioNegro

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

@app.get("/himnarioNegro")
def listar_himnarioNegro():
    return himnarioNegro