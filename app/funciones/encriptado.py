"""
Este modulo trabajará una encriptacion simetrica!
"""
from cryptography.fernet import Fernet

def encriptando_texto(mensaje:bytes,llave:bytes)->str:
    """
    Esta funcion hace un encriptado simetrico
    Parametros:
        - mensaje (bytes): es el mensaje a ser encriptado
        - llave (bytes): es la llave de encriptación
    Retorna:
        - (str): Mensaje encriptado
    """
    #llave = Fernet.generate_key()
    entorno_cifrado = Fernet(llave)

    mensaje_encriptado = entorno_cifrado.encrypt(mensaje)
    return mensaje_encriptado

def desencriptando_texto(mensaje_encriptado:str,llave:str)->str:
    """funcion para desencriptar mensaje con una llave

    Args:
        mensaje_encriptado (str): mensaje raro, listo para ser traducido a un lenguaje mas comun
        llave (str): llave de encruptacion/desencriptación

    Returns:
        str: mensaje desencriptado
    """
    entorno_cifrado = Fernet(llave)
    mensaje_desencriptado = entorno_cifrado.decrypt(mensaje_encriptado)
    return mensaje_desencriptado
