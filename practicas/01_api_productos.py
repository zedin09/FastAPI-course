from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    id: str | None
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

app = FastAPI()

productos = []

@app.get('/')
def index():
    return{'message': "Bienvenidos a la api de productos"}

@app.get('/producto')
def obtener_productos():
    return productos