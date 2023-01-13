from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return{'message': "Bienvenidos a la api de productos"}