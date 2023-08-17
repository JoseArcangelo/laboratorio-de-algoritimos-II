lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
l2 = []
contador = len(lista)

for i in range(len(lista)):
    contador = contador - 1
    l2.append(lista[contador])
    
print(l2)
