"""
Crea un programa que imprima la tabla de multiplicar de un número ingresado por el 
usuario
"""
import os
yes = ["yes","si","y","s"]
no = ["no","parar","stop"   ]
n = input("pulse enter para comenzar: ")
while n != 0:
    n = int(input("""


    ingrese un numero


    """))
    os.system("cls")
    for i in range(1, 11):
        r = n * i
        print(f"{n} x {i} = {r}")

    x = input("quieres continuar?: ")
    if x.lower() == "no" or x.lower() == "parar" or x.lower() == "stop" or x.lower() == "n":
        os.system("cls")
        break
    if x.lower() == "yes" or x.lower() == "si" or x.lower() == "y" or x.lower() == "s":
        os.system("cls")
        pass


