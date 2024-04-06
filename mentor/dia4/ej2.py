class archivo:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def create(self):
        return open(self.name + self.extension, 'w')
    
    def read(self):
        return open(self.name + self.extension, 'r')
    
    def anex(self):
        return open(self.name + self.extension, 'a')

bltc = archivo("biblioteca", ".txt")

class biblioteca:
    def __init__(self, ID_libro, nombre, autor, categoria):
        self.ID_libro = ID_libro
        self.nombre = nombre
        self.autor = autor
        self.categoria = categoria

    def archivo(self):
        f = bltc.create()
        f.write("ID_libro, nombre, autor, categoria\n")  
        f.close()
    
    def entrada(self):

        f = bltc.read()
        for linea in f:
            print(linea.strip()) 
        f.close()
    
    def write(self):

        f = bltc.anex()
        f.write(f"{self.ID_libro}, {self.nombre}, {self.autor}, {self.categoria}\n")
        f.close()

#   "frutas"
#
#