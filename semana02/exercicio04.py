matriz = [[1, 12, 7], [7, 5, 10], [2, 10, 9]]
media_total = 0
contador = 0
media_linha = 0
l = 0

for linha in matriz:
    for elemento in linha:
        contador += 1
        media_total += elemento
        media_linha += elemento
        if contador % 3 == 0:
            media_linha = media_linha / len(linha)
            l +=1
            print("A media da linha", l, "é:", media_linha)
            media_linha = 0
            
media_total = media_total / contador
print("Media da matriz:", media_total)
