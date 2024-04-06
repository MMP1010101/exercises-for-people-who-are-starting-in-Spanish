
try:
    num = int(input("ingrese un numero: "))


    if num > 0:
        print(f"{num} es positivo")
    elif num < 0:
        print(f"{num} es negativo")
    else:
        print("es neutro")
except:
    print("as solicitado un valor incorrecto")