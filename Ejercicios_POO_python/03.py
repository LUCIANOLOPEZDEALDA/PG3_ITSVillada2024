class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def es_equilatero(self):
        return self.lado1 == self.lado2 == self.lado3


lado1 = float(input("Ingrese el lado 1 del triángulo: "))
lado2 = float(input("Ingrese el lado 2 del triángulo: "))
lado3 = float(input("Ingrese el lado 3 del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

print("El lado mayor es:", triangulo.obtener_lado_mayor())

if triangulo.es_equilatero():
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")