class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.realizar_operaciones()

    def realizar_operaciones(self):
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        suma = self.num1 + self.num2
        print(f"Suma: {self.num1} + {self.num2} = {suma}")

    def resta(self):
        resta = self.num1 - self.num2
        print(f"Resta: {self.num1} - {self.num2} = {resta}")

    def multiplicacion(self):
        multiplicacion = self.num1 * self.num2
        print(f"Multiplicación: {self.num1} * {self.num2} = {multiplicacion}")

    def division(self):
        if self.num2 != 0:
            division = self.num1 / self.num2
            print(f"División: {self.num1} / {self.num2} = {division}")
        else:
            print("Error: No se puede dividir por cero.")

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

operaciones = Operaciones(num1, num2)
