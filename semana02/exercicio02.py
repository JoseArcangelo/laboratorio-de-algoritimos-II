l = [100, 2, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 100]
l_unicos = []
l_repetidos = []

for i in l:
    if i not in l_unicos and i not in l_repetidos:
        l_unicos.append(i)
    elif i in l_unicos:
        l_unicos.remove(i)
        l_repetidos.append(i)

print("Repetidos:",l_repetidos,"Unicos:", l_unicos)

