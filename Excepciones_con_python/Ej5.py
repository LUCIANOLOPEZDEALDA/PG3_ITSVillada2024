texto = input("Escriba aqui: ")
try:
    with open("archivo.txt", "w") as archivo:
        archivo.write(texto)
except ValueError as e:
    print("Se produjo un error", e)