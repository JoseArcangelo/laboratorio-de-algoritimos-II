matriz = [
    [2,  5,  7],
    [5,  1,  8],
    [7,  8,  9],
]
resposta = True
            
for linha in range(len(matriz)):
    for elemento in range(len(matriz[linha])):
        if matriz[linha][elemento] != matriz[elemento][linha] or len(matriz) != len(matriz[linha]):
            resposta = False
            break
        else:
            resposta = True
print(resposta)
