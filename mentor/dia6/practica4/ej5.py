"""
Ejercicio 5
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor
máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el
mínimo, utilizando la función anterior
"""

def descomponerEnPrimos(n):
    factores = []
    for primo in [2, 3, 5]:
        while n % primo == 0:
            n = n // primo  
            factores.append(primo)
    return factores if factores else [n]  

def calcularMaxMin(n1: int, n2: int):
    factores_n1 = descomponerEnPrimos(n1)
    factores_n2 = descomponerEnPrimos(n2)

    todos_los_factores = factores_n1 + factores_n2  
    if not todos_los_factores:  
        return None  
    return max(todos_los_factores), min(todos_los_factores)

# Ejemplo de llamada a la función
print(descomponerEnPrimos(8))  
print(calcularMaxMin(453, 231))   
