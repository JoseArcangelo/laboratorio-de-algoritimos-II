matriz_1 = [[41, 1, 9], [1, 113, 2], [7, 1, 12]]
matriz_2 = [[2, 2, 1], [2, 2, 1], [2, 2, 1]]
matriz_3 = []
contador1 = 0
contador2 = 0

for linha in matriz_1:
    matriz_3.append([])

    for elemento in linha:
        matriz_3[contador1].append(elemento + matriz_2[contador1][contador2])
        contador2 += 1

        if contador2 == 3:
            contador1 += 1
            contador2 = 0
            
print(matriz_3)
