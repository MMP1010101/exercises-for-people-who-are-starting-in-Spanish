"""
La función EscribirCentrado(texto) toma 
un texto como parámetro y lo imprime centrado en la pantalla, asumiendo una anchura de 80 columnas. 
También subraya el mensaje utilizando el carácter "=".
"""

def EscribirCentrado(texto):
    anchura = 80
    space = " " * anchura
    print(space + "=" * len(texto) )


print(str(3))