"""Este es el modulo principal donde habrá la creacion y disposición de una API"""
from fastapi import FastAPI
from funciones.cifrado_cesar import cifrado_cesar

app = FastAPI()

@app.get("/")
def home():
    """
    Funcion principal de API
    """
    return {"Hola":"Mundo123"}

@app.get("/cifrado-cesar")
def url_cifrado_cesar(texto,clave):
    """
    URL para hacer encriptado CESAR
    """
    salida = cifrado_cesar(texto,int(clave))
    return {"mensaje_cifrado":salida}
