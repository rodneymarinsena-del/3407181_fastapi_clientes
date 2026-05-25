from fastapi import FastAPI
app = FastAPI()

Lista_Clientes = [{"nombre": "Juan",
                    "edad": 25,
                    "descripcion": "n.a"},
                    {"nombre": "Maria",
                    "edad": 30,
                    "descripcion": "n.a"}]

@app.get("/cliente")
def Cliente_Nuevo():
    return {"Hello": "Hola Cliente nuevo"}

@app.get("/Lista_Clientes")
def Lista_Clientes():
    return {"Clientes": Lista_Clientes}

@app.post("/Crear_Clientes")
def Crear_Clientes():
    return {"message": "Cliente creado exitosamente"}

@app.put("/Editar_Clientes")
def Editar_Clientes():
    return {"message": "Cliente editado exitosamente"}

@app.delete("/Eliminar_Clientes")
def Eliminar_Clientes():
    return {"message": "Cliente eliminado exitosamente"}