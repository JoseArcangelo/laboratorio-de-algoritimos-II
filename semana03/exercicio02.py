matriz = [
    [1, 2, 3, 4, 5],
    [1, 1, 1, 4, 5],
    [9, 2, 7, 4, 5],
    [2, 2, 3, 5, 5],
    [1, 2, 6, 4, 6]
    ]

soma = 0
for line in range(len(matriz)):
    for colunm in range(len(matriz[line])):
        if line - colunm > 0:
            soma += matriz[line][colunm]
            
print("Resultado da soma:", soma)
        
