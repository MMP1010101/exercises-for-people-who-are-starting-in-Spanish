from dia3.ej5  import Persona

dinero = int(input("ingrese su dinero: "))
edad = int(input("Ingrese su edad: "))
Paco = Persona(dinero, edad)

print(Paco.tributar())