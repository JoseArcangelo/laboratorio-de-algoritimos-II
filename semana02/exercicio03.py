matriz = [[1, 17, 14], [7, 5, 11], [2, 10, 9]]
resultado = 0
maiorValor = 0
contador = 0

for linha in matriz:
    for elemento in linha:
        contador += 1
        if elemento > maiorValor:
            maiorValor = elemento
        if contador == 3:
            resultado += maiorValor
            contador = 0
            maiorValor = 0
           
print("Resultado:",resultado)
            
        
