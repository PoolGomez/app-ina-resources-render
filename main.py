from fastapi import FastAPI
from data.Sedes import sedes
from data.Himnos import himnos
from data.Himnarios import himnarios
from docs import tags_metadata
from routes.user import user
from routes.authentication import authentication
from routes.sede import sede
from routes.himnario import himnario
from routes.himno import himno

app = FastAPI(
    title="REST API APPINA",
    descripcion="Rest API usando fastapi y mongo db",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(user)
app.include_router(authentication)
app.include_router(sede)
app.include_router(himnario)
app.include_router(himno)

@app.get("/")
def index():
    return "index"

# @app.get("/membresia")
# def listar_miembros():
#     usuarios = pd.read_csv("./data/membresia.csv")
#     return json.loads(usuarios.to_json(orient='records'))

# @app.get("/sedes")
# def listar_sedes():
#     return sedes

# @app.get("/himnos")
# def listar_himnos():
#     return himnos

# @app.get("/himnarios")
# def listar_himnarios():
#     return himnarios