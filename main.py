from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


# 1. Creación del Modelo
class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

# 2. Variable para almacenar los clientes
lista_clientes: List[Cliente] = []

# 3. Endpoint para listar todos los clientes
@app.get("/clientes")
def listar_clientes():
    return lista_clientes

# 4. Endpoint para listar un solo cliente por su ID
@app.get("/clientes/{cliente_id}")
def listar_cliente(cliente_id: int):
    for i, objeto_cliente in enumerate(lista_clientes):
        if objeto_cliente.id == cliente_id:
            return objeto_cliente
    return None

# 5. Endpoint para crear un nuevo cliente
@app.post("/clientes")
def crear_cliente(datos_del_cliente: Cliente):
    lista_clientes.append(datos_del_cliente)
    return datos_del_cliente