def find_element(lista, indice):
  try:
    if indice > len(lista) - 1 or indice < 0:
      raise IndexError("Valor inválido")
    print(lista[indice])
    
  except IndexError as e:
    print(e)

lista = ["a", "b", "c", "d", "e"]
try:
  indice = int(input("Informe o indice: "))
except ValueError:
  print("Valor inválido")
find_element(lista, indice)
