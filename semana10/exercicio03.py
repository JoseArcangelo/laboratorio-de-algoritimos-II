def fazer_copia_arquivo():
  name = input("Informe o nome do arquivo: ")
  try: 
    file = open(f'exercicio03/{name}', 'r')
  except BaseException as e:
    print(f"[ERRO] {e}")
    fazer_copia_arquivo()

  file_list = file.readlines()
  file.close() 
  
  new_file = open(f'exercicio03/copia_{name}.txt', 'w')
  for line in file_list:
    new_file.write(str(line))
  new_file.close()

def main():
  fazer_copia_arquivo()
main()
