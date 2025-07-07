from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡App FastAPI en Render funcionando con elegancia!"}

@app.get("/saludo/{nombre}")
def saludo_personalizado(nombre: str):
    return {"mensaje": f"Hola, {nombre}. Esta app está corriendo en Render con FastAPI."}