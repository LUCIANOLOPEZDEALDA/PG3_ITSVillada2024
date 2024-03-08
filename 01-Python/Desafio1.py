def triangulo(ancho, alto, caracter):
    for i in range(1, alto + 1):
        linea = caracter * i
        print(linea.center(ancho))

ancho = int(input("Ingrese el ancho del triángulo: "))
alto = int(input("Ingrese el alto del triángulo: "))
caracter = input("Ingrese el carácter a utilizar en el dibujo: ")

triangulo(ancho, alto, caracter)