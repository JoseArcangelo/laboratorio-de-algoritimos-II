def find_element(lista, indice):
    try:
        if indice > len(lista) - 1 or indice < 0:
            raise IndexError("Valor inválido")
        return lista[indice]
    
    except IndexError as e:
        print(e)

lista = ["a", "b", "c", "d", "e"]

while True:
    try:
        indice = int(input("Informe o indice: "))
        break
    except ValueError:
        print("Valor inválido")
    except BaseException:
        print("[ERRO]")

  
elemento = find_element(lista, indice)
if elemento != None:
  print(elemento)
