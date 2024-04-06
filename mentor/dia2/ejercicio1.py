"""
Ejercicio 1.
Las materias impartidas por el centro educativo son: Matemáticas, Física, Química, Historia y 
Lengua, realice un programa le debe permitir al usuario ver las materias en pantalla, agregar y 
eliminar, materias en caso que sea necesario
"""
start = ''
pregunta = "si"
while pregunta == "si":
    materia = ["Matemáticas", "Física", "Lengua", "Química", "Historia"]
    start = input("que quieres hacer? (agregar/a | eliminar/e) | (salir/s)").lower()
    if start == "a":
        name = input("como la quieres llamar?: ")
        materia.append(name)
        for i in materia:
            print("---")
            print(f"| {i} |")
            
        pregunta = input("""

Que quieres hacer?:""")
        
    elif start == "e":
        name = input("como la quieres eliminar?: ")
        materia.remove(name)
        print(materia)
        pregunta = input("""

Que quieres hacer?:""")
    else:
        print("es opcion incorrecta: ")
    


