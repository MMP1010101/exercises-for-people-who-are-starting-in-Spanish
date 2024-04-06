"""
Esta sacado de internet este contador
Lo intente de muchas maneras con el "open" pero no encontre la manera
"""


def incrementar_contador():
    try:
        with open("contador.txt", "r") as archivo:
            contador = int(archivo.read())
    except FileNotFoundError:
        contador = 0

    contador += 1
    with open("contador.txt", "w") as archivo:
        archivo.write(str(contador))

    return contador


if __name__ == '__main__':
    incrementar_contador()