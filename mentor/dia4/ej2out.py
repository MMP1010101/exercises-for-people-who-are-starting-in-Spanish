import ej2 
import ej2id

objecto = ej2.biblioteca
ID = ej2id.incrementar_contador()

name = input("ingrese el nombre del libro: ")
autor = input("ingrese el nombre del autor: ")
categoria = input("ingrese la categoria del libro: ")

libreria = ej2.biblioteca(ID, name, autor, categoria)

if __name__ == '__main__':
    libreria.archivo() #quitarlo cuando se cree el archivohgc 
    libreria.write()
    libreria.entrada() 