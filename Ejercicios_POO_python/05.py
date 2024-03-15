class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} debe pagar impuestos.")
        else:
            print(f"{self.nombre} no debe pagar impuestos.")


persona1 = Persona("", 0)
persona1.cargar_datos()
persona1.imprimir()

empleado1 = Empleado("", 0, 0)
empleado1.cargar_datos()
empleado1.imprimir()
empleado1.sueldo = float(input("Ingrese el sueldo del empleado: "))
empleado1.pagar_impuestos()
