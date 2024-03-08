def rectangulo(ancho, alto, letra):
    for i in range(alto):
        for j in range(ancho):
            print(letra, end=" ")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter = input("Carácter a utilizar: ")
rectangulo(anchura, altura, caracter)