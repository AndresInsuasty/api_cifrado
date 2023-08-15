"""
Aqui se prueba la funcion de encriptado simetrico
"""
import pytest
from app.funciones.encriptado import encriptando_texto
from cryptography.fernet import Fernet

@pytest.mark.parametrize(
        "mensaje,llave",
        [
        (
        b"a",
        b"UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
        ),

        (
        b"b",
        b"UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
        ),

        (
        b"Este es mi curso de python",
        b"UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
        )
        ])
def test_encriptando_texto(mensaje,llave):
    entorno_cifrado = Fernet(llave)
    salida = encriptando_texto(mensaje,llave)
    mensaje_desencriptado = entorno_cifrado.decrypt(salida)
    assert mensaje_desencriptado == mensaje