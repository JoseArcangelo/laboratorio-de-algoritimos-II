def ler_arquivo():
  palavra = str(input("Informe a palavra que deseja encontrar: "))
  result = []
  file = open('exercicio02/texto.txt', 'r')
  contador = 0
  for line in file:
    line = str(line)
    contador += 1
    if palavra in line:
      result.append(f"Linha {contador}")
  file.close()
  return result

def main():
  result = ler_arquivo()
  print("Sua palavra foi encontrada nas seguintes linhas: ")
  for line in result:
    print(line)
main()
