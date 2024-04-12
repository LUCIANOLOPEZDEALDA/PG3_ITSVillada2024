def suma():
    suma_total = 0
    while True:
        try:
            valor1 = int(input("Ingrese el primer numero: "))
            valor2 = int(input("Ingrese el segundo numero: "))
            suma_total = valor1 + valor2
            print(suma_total)
            while True:
                pregunta = input("Desea continuar agregando valores? s/n: ")
                if pregunta.lower() == "s":
                    try:
                        nuevo_valor = int(input("Ingresa el valor: "))
                        suma_total += nuevo_valor
                        print(suma_total)
                    except ValueError:
                        print("Ingresaste un caracter no numerico")
                elif pregunta.lower() == "n":
                    return
                else:
                    print("Opción no válida. Por favor ingrese 's' para seguir sumando o 'n' para terminar.")
        except ValueError: 
            print("Ingresaste un caracter no numerico")
suma()
