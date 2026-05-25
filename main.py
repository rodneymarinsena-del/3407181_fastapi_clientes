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
def listar_clientes():
    return lista_clientes


@app.post("/clientes",response_model=list[Cliente])
def crear_clientes(datos_cliente:  Cliente):
    Cliente.validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return Cliente_val


@app.put("/clientes")
def editar_clientes(id:int,datos_cliente:Cliente):

    return {"mensaje": "Cliente Editado"}


@app.delete("/clientes/{id}")
def eliminar_clientes():
    return {"mensaje": "Cliente eliminado"}
