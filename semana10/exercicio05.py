def ler_arquivo():
  file = open('exercicio05/exemplo.txt', 'r')
  list_lines = file.readlines()
  file.close()
  return list_lines

def inverter_list_lines(list_lines):
  l_auxiliary = []
  for i in list_lines:
    l_auxiliary.insert(0, i)
  list_lines = l_auxiliary
  return list_lines

def criar_arquivo_invertido(list_lines):
  file = open('exercicio05/copia_invertida_exercicio05.txt', 'w')
  file.writelines(list_lines)
  file.close

def main():
  list_lines = ler_arquivo()
  list_lines = inverter_list_lines(list_lines)
  list_lines[0] = f'{list_lines[0]}'
  list_lines[-1] = list_lines[-1].replace("\n", "")
  criar_arquivo_invertido(list_lines)
main()
