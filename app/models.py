from pydantic import BaseModel

class ClienteIn(BaseModel):
    nombre: str
    email: str | None = None

class Cliente(ClienteIn):
    id: int
