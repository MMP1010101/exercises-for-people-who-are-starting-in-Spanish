
"""
esarrolla un programa que sume los números pares del 1 al 100 utilizando un bucle 
for
"""
lista = []
outpud = int(input("ingrese el numero 100"))
for i in range(0, outpud + 1):
    if i % 2 == 0:
        lista.append(i)
        print(lista)
n = 0
for i in lista:
    n += i

print(f"""


    La respuesta es {n}


""")
        
    



        