lista = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10]
l_repitidos = []
l_unicos = []
lista_copia = lista[:]

for a in lista_copia:
    lista_copia.remove(a)
    for b in lista_copia:
        if a == b:
            l_repitidos.append(b)
        else
                      
                
print(l_repitidos)
print(l_unicos)
           
