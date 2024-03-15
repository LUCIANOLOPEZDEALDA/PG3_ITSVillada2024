class Persona:

    def inicializar(self,nombre):
        self.nombre = nombre

    def imprimir(self):
        print("Nombre",self.nombre)

persona1=Persona()
persona1.inicializar("Jorge")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Raul")
persona2.imprimir()