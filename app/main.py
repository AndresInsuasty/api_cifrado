"""Este es el modulo principal"""
from funciones.cifrado_cesar import cifrado_cesar

MENSAJE = "Este es mi mensaje"
CLAVE = 2

resultado = cifrado_cesar(MENSAJE,CLAVE)
print(resultado)
