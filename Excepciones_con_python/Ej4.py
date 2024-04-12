def division():
    division_total = 0
    while True:
        try:
            valor1 = int(input("Ingrese el primer numero: "))
            valor2 = int(input("Ingrese el segundo numero: "))
            division_total = valor1 / valor2
            print(division_total)
        except ZeroDivisionError: 
            print("No puedes dividir por cero")
        except ValueError:
            print("No puedes ingresar caracteres no numericos")
division()
