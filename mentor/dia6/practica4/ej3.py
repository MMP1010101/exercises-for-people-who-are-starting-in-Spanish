"""
Ejercicio 3
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y
mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la
temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el
número de días que se van a introducir.

"""

def medTemEX(n1: int, n2: int):
    n = 0
    x = 0
    lista = [n1, n2]
    for j  in lista:
        if j > 0:
            x = x + 1
    for i in lista:
        n += i
    return n / x

def medTemABS(n1: int, n2: int):
    n = 0
    x = 0
    lista = [n1, n2]
    for j  in lista:
        if j > 0:
            x = x + 1
    for i in lista:
        n += i
    return n // x

def medTemAPX(n1: int, n2: int):
    clima = medTemEX(n1, n2)
    return round(clima)

