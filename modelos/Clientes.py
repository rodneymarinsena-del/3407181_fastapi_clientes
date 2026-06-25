from pydantic import BaseModel

# Clase base con los datos comunes (sin ID)
class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

# Clase para la respuesta (hereda de ClienteBase y añade el ID)
class Cliente(ClienteBase):
    id: int | None = None

# Clase para la creación (hereda de ClienteBase, no requiere nada extra por ahora)
class ClienteCrear(ClienteBase):
    pass