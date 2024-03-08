def c_vocales():
    frase = input("Ingrese una frase/palabra: ")
    contador = 0
    for i in frase:
        if i in "aeiouAEIOU":
            contador = contador + 1
    print("La cantidad de vocales que hay son",contador)

c_vocales()