from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes = []

#crear Clase MODELO
class Cliente(BaseModel):
    Id: int
    nombre: str
    edad: int
    descripcion: str 


@app.get("/clientes")
def listar_clientes(datos_cliente:  Cliente):
    return {"clientes": lista_clientes}


@app.post("/clientes")
def crear_clientes(datos_cliente:  Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Cliente creado"}


@app.put("/clientes")
def editar_clientes():
    return {"mensaje": "Cliente Editado"}


@app.delete("/clientes")
def eliminar_clientes():
    return {"mensaje": "Cliente eliminado"}
