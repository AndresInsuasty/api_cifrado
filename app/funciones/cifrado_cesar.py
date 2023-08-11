"""
Modulo para hacer cifrado cesar
"""
def cifrado_cesar(texto, clave):
    """función que implementa algoritmo de cifrado cesar

    Args:
        texto (str): texto a ser procesado/cifrado
        clave (int): clave de cifrado

    Returns:
        str: texto procesado/cifrado
    """
    # alfabeto
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    # texto cifrado
    texto_cifrado = ""
    # recorrer texto
    for letra in texto.upper():
        # si la letra está en el alfabeto
        if letra in alfabeto:
            # obtener posición de la letra en el alfabeto
            posicion = alfabeto.index(letra)
            # obtener nueva posición
            nueva_posicion = (posicion + clave) % len(alfabeto)
            # obtener nueva letra
            nueva_letra = alfabeto[nueva_posicion]
            # añadir nueva letra al texto cifrado
            texto_cifrado += nueva_letra
        else:
            # añadir letra al texto cifrado
            texto_cifrado += letra
    # devolver texto cifrado
    return texto_cifrado
