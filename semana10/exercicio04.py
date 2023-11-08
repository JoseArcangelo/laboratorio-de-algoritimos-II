def varificar_enderecos():
  validos = []
  invalidos = []
  
  file = open('exercicio04/enderecos.txt', 'r')
  list_auxiliry = []
  
  for endereco in file:
    list_auxiliry.append(endereco)
    if " " in list_auxiliry[0]:
      list_auxiliry = ' '.join(list_auxiliry)
      list_auxiliry = list_auxiliry.split(" ")
  file.close()

  for id in list_auxiliry:
    id = id.strip()
    partes = id.split(".")
    verification = True
    counter = 0

    for element in partes:
      if len(partes) != 4:
        verification = False
        break
      if element != "":
        element = int(element)
        counter += 1
        if counter == 1 and (element >= 1 or element <= 255):
          verification = True
          
        if counter == 1 and( element < 1 or element > 255):
          verification = False
          break
        
        elif counter != 1 :
          if element < 0 or element > 255:
            verification = False
            print(element)
            break

    if verification == False:
      invalidos.append(id)
    else:
      validos.append(id)
    
  
  return validos, invalidos
  
def main():

  validos, invalidos = varificar_enderecos()
  print("--INVÁLIDOS--")
  for a in invalidos:
    print(a)
  print("\n--VÁLIDOS--")
  for b in validos:
    print(b)
main()
