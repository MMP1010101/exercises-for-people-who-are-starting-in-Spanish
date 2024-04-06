"""
Crea un programa que solicite al usuario ingresar un número y luego imprima si es 
primo o no.

"""

outpud = int(input("introduce un numero: "))
n = outpud; n -= 1
suma = []
while n != 0:
    suma.append(0)
    n = 2 / n
    print(n)
print(suma[-1])

