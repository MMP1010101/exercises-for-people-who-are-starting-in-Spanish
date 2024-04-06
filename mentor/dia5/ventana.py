from tkinter import *

vt = Tk() #ventana
vt.title("tkinter") #nombre
vt.geometry("450x500") #tamaño
vt.resizable(False, False) #para que no se pueda cambiar el tamaño
vt.config(bg="lightblue")

BarraMenu = Menu(vt)
archivoMenu = Menu(BarraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=vt.quit)

editarmenu = Menu(BarraMenu, tearoff=0)
editarmenu.add_command(label="cortar")
editarmenu.add_command(label="copiar")
editarmenu.add_command(label="pegar")

ayudaMenu = Menu(BarraMenu, tearoff=0)
ayudaMenu.add_command(label="ayuda")
ayudaMenu.add_separator()
ayudaMenu.add_command(label="acerca de...")

BarraMenu.add_cascade(label="Archivo", menu=archivoMenu)
BarraMenu.add_cascade(label="Editar", menu=editarmenu)
BarraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

vt.config(menu=BarraMenu)
vt.mainloop()