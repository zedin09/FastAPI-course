from fastapi import FastAPI
from pydantic import BaseModel

class Producto(BaseModel):
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

@app.post('/producto')
def crear_producto(producto: Producto):
    productos.append(producto)
    return {'message': "Producto creado satisfactoriamente"}