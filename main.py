from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#crear Clase MODELO
class Cliente(BaseModel):
    Id: int
    nombre: str
    edad: int
    descripcion: str 

lista_clientes:list[Cliente]  =[]

@app.get("/clientes",response_model=list[Cliente])
def listar_clientes(datos_cliente:  Cliente):
    return lista_clientes


@app.post("/clientes",response_model=list[Cliente])
def crear_clientes(datos_cliente:  Cliente):

    lista_clientes.append(datos_cliente)
    return datos_cliente


@app.put("/clientes")
def editar_clientes():
    return {"mensaje": "Cliente Editado"}


@app.delete("/clientes")
def eliminar_clientes():
    return {"mensaje": "Cliente eliminado"}
