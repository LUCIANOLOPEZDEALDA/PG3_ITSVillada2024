class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre",self.nombre)
        print("Nota",self.nota)

    def estado(self):
        if self.nota >= 6:
            print("Regular")
        else:
            print("Libre")

Alumno1=Alumno()
Alumno1.inicializar("Jorge",4)
Alumno1.imprimir()
Alumno1.estado()

Alumno2=Alumno()
Alumno2.inicializar("Raul",9)
Alumno2.imprimir()
Alumno2.estado()