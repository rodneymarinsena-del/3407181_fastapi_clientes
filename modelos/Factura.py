
from pydantic import BaseModel

class FacturaBase (BaseModel):
    fecha: str
    vr_total: float
#calcular(cantidad *vr_unitario)
    cliente: Cliente # esta es la relacion con el cliente(objeto)
class FacturaCrear (FacturaBase):
    pass
I
class Factura (FacturaBase):
    id: int | None = None