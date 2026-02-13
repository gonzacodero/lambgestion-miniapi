from .models import Cliente, ClienteIn

_clientes: list[Cliente] = []
_next_id = 1

def listar_clientes() -> list[Cliente]:
    return _clientes

def crear_cliente(data: ClienteIn) -> Cliente:
    global _next_id
    cliente = Cliente(id=_next_id, **data.model_dump())
    _clientes.append(cliente)
    _next_id += 1
    return cliente
