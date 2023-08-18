matriz = [
    [2,  5,  7],
    [5,  1,  8],
    [7,  8,  9],
]
resposta = True
parar = False
            
for linha in range(len(matriz)):
    if parar == True:
        break
    for elemento in range(len(matriz[linha])):
        if matriz[linha][elemento] != matriz[elemento][linha] or len(matriz) != len(matriz[linha]):
            resposta = False
            parar = True
            break
        else:
            resposta = True
    
print(resposta)
