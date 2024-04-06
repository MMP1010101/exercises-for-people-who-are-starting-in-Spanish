from tkinter import * 

root = Tk()
root.title("Botones")
root.geometry("800x800")
root.resizable(False, False)
root.config(bg="#02F58D")

barra = Menu(root)
archivo = Menu(barra, tearoff=0) #ventana 1 o valor 0
archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_separator()
archivo.add_command(label="salir", command=root.quit)

editar = Menu(barra, tearoff=0)
editar.add_command(label="cortar")
editar.add_command(label="copiar")
editar.add_command(label="pegar")

ayuda = Menu(barra, tearoff=0)
ayuda.add_command(label="ayuda")
ayuda.add_separator()
ayuda.add_command(label="hacerca de...")

barra.add_cascade(label="Archivo", menu=archivo)
barra.add_cascade(label="Editar", menu=editar)
barra.add_cascade(label="Ayuda", menu=ayuda)

root.config(menu=barra)

texto = Label(root, text="Hola a todos", font=("Times new Roman",18,"bold", "roman"), bg="blue", fg="red")
texto.place(x=190, y=180)
root.mainloop()
