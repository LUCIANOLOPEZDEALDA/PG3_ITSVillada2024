def obtenermes():
    while True:
        meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
        try:
            numero_mes = int(input("Ingrese el número de mes (1-12): "))
            nombre_mes = meses[numero_mes - 1]
            print("El nombre del mes es:", nombre_mes)
        except IndexError:
            print("Error: El número de mes ingresado está fuera del rango válido.")

obtenermes()
