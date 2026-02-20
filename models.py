from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class ClienteCreate(BaseModel):
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    plan_contratado: str = 'Mensual'
    telefono: Optional[str] = None
    correo: Optional[EmailStr] = None
    direccion: Optional[str] = None

class ClienteUpdate(ClienteCreate):
    activo: bool  # Solo para actualización

class Cliente(ClienteCreate):
    id_cliente: int
    activo: bool