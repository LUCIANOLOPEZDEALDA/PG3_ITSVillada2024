def funcion(numerob,i,lista):
    for i in range (len(lista)):
        if lista[i] == numerob:
            print('el indice del', lista[i], 'se encuentra en la posicion', i)
        else:
            i+1
i=0
lista=[8,12,9,45]
print(lista)
numerob = int(input('elegi un numero de la lista: '))
funcion(numerob,i,lista)