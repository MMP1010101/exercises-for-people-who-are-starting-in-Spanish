"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
superiores a 1000 mensuales Escribir un programa que pregunte al usuario su edad y sus ingresos € . 
mensuales y muestre por pantalla si el usuario tiene que tributar o no .
"""
class Persona:
    def __init__(self, dinero, edad):
        self.dinero = dinero
        self.edad = edad

    def tributar(self):
        if self.edad > 16 and self.dinero >= 1000:
            return "tienes que tributar"
        else:
            return "no tienes que tributar"

def main():
    restriccion = 16

    print("¿Cuál es tu edad?: ")
    edad = int(input())

    print("¿Cuánto es tu ingreso mensual en euros?: ")
    ingresos = float(input())

    persona = Persona(ingresos, edad)

    print(persona.tributar())

if __name__ == "_main_":
    main()