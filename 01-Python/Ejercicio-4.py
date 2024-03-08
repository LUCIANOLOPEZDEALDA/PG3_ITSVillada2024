def ordenar():
    lista = [10,2,1,7,9,3,6,8,4,5]
    for recorrido in range(1,len(lista)):
        for posicion in range(len(lista) - recorrido):
            if lista[posicion] < lista[posicion + 1]:
                temp = lista[posicion]
                lista[posicion] = lista[posicion + 1]
                lista[posicion + 1] = temp
    print (lista)
    
ordenar()