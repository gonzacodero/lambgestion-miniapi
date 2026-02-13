from fastapi import FastAPI
from .models import Cliente, ClienteIn
from .store import listar_clientes, crear_cliente

app = FastAPI(title="LambGestion Mini API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/clientes", response_model=list[Cliente])
def get_clientes():
    return listar_clientes()

@app.post("/clientes", response_model=Cliente, status_code=201)
def post_cliente(payload: ClienteIn):
    return crear_cliente(payload)
