from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from uuid import uuid4 as uuid

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

#? CREATE
@app.post('/producto')
def crear_producto(producto: Producto):
    producto.id = str(uuid())
    productos.append(producto)
    return {'message': "Producto creado satisfactoriamente"}

#? READ
@app.get('/producto')
def obtener_productos():
    return productos

@app.get('/producto/{producto_id}')
def obtener_producto_por_id(producto_id: str):
    resultado = list(filter(lambda p: p.id == producto_id, productos))
    
    if len(resultado):
        return resultado[0]
    
    raise HTTPException(status_code=404, detail=f"El producto con el id {producto_id} no fue encontrado")

#? UPDATE
@app.put("/products/{producto_id}")
def actualizar_producto(producto_id: str, producto: Producto):
    resultado = list(filter(lambda p: p.id == producto_id, productos))
    
    if len(resultado):
        p_encontrado = productos[0]
        p_encontrado.nombre = producto.nombre
        p_encontrado.precio_compra = producto.precio_compra
        p_encontrado.precio_venta = producto.precio_venta
        p_encontrado.proveedor = producto.proveedor
        
        return p_encontrado
    
    raise HTTPException(status_code=404, detail=f"El producto con el id {producto_id} no fue encontrado")
    

#? DELETE
@app.delete('/producto/{producto_id}')
def eliminar_producto_por_id(producto_id: str):
    resultado = list(filter(lambda p: p.id == producto_id, productos))
    
    if len(resultado):
        producto = productos[0]
        productos.remove(producto)
        
        return {'message': f'El producto con el id {producto_id} fue eliminado'}
    
    raise HTTPException(status_code=404, detail=f"El producto con el id {producto_id} no fue encontrado")