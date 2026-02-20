from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from models import ClienteCreate, ClienteUpdate
from crud import (
    listar_clientes, crear_cliente, obtener_cliente,
    actualizar_cliente, eliminar_cliente
)

app = FastAPI(
    title="API GYM Rufito",
    description="API REST para la gestión de clientes y planes del gimnasio",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# =========================
# CLIENTES
# =========================

@app.get("/api/clientes")
def get_clientes():
    return listar_clientes()

@app.get("/api/clientes/{id_cliente}")
def get_cliente(id_cliente: int):
    cliente = obtener_cliente(id_cliente)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.post("/api/clientes")
def post_cliente(cliente: ClienteCreate):
    nuevo_id = crear_cliente(cliente)
    return obtener_cliente(nuevo_id)


@app.put("/api/clientes/{id_cliente}")
def put_cliente(id_cliente: int, cliente: ClienteUpdate):

    cliente_actual = obtener_cliente(id_cliente)

    if not cliente_actual:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    actualizar_cliente(id_cliente, cliente)

    return {"mensaje": "Cliente actualizado correctamente"}


@app.delete("/api/clientes/{id_cliente}")
def delete_cliente(id_cliente: int):
    if not obtener_cliente(id_cliente):
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    eliminar_cliente(id_cliente)
    return {"mensaje": "Cliente eliminado correctamente"}


# ====================================================
# 🔥 ENDPOINT SOLO PARA ACTUALIZAR EL PLAN
# ====================================================

class PlanUpdate(BaseModel):
    plan_contratado: str


@app.put("/api/clientes/{id_cliente}/plan")
def actualizar_plan(id_cliente: int, datos: PlanUpdate):

    cliente_actual = obtener_cliente(id_cliente)

    if not cliente_actual:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    if cliente_actual["plan_contratado"] == datos.plan_contratado:
        raise HTTPException(
            status_code=400,
            detail="El cliente ya tiene ese plan contratado"
        )

    cliente_update = ClienteUpdate(
        nombre=cliente_actual["nombre"],
        apellidos=cliente_actual["apellidos"],
        fecha_nacimiento=cliente_actual["fecha_nacimiento"],
        plan_contratado=datos.plan_contratado,
        telefono=cliente_actual.get("telefono"),
        correo=cliente_actual.get("correo"),
        direccion=cliente_actual.get("direccion"),
        activo=cliente_actual["activo"]
    )

    actualizar_cliente(id_cliente, cliente_update)

    return {"mensaje": "Plan actualizado correctamente"}