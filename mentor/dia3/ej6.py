"""
Ejercicio 6 
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre El . 
grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto Escribir un programa que pregunte al usuario su nombre y . 
sexo y muestre por pantalla el grupo que le corresponde
"""

def sexo():
    lista = []
    continuar = "si"
    while continuar.lower() == "si":
        sex = 0  
        insert_name_spanish = "Ingrese su nombre: "
        pregunta_sex = "¿Eres hombre o mujer? (h/m): "

        name = input(insert_name_spanish)
        while sex != 11011 and sex != 11001:
            respuesta_sex = input(pregunta_sex)
            if respuesta_sex.lower() in ["h", "hombre"]:
                sex = 1011
                lista.append((name, sex)) #lo de la tupla lo e buscado pero ha hora tengo claro que se puede convertir lo de tuplas en otras iterables
                sex = sex + 10000                           #ejemplo con:
            elif respuesta_sex.lower() in ["m", "mujer"]:       #name = i; sex = j
                sex = 1001
                lista.append((name, sex))  
                sex = sex + 10000  
        continuar = input("¿Quieres continuar? (si/no): ")
    for i, j in lista:           
        if (j == 1001 and i[0].lower() < 'm') or (j == 1011 and i[0].lower() > 'n'): #aqui pongo parentesis para que se vea como otros lenguajes xd
            grupo = "A"
        else:
            grupo = "B"
        print(f"{i}, perteneces al grupo {grupo}.", end=" | ")

sexo()
