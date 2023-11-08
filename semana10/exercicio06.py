def media(nomes, notas):
  total_notas = 0
  ## Formar uma lista com todos os nomes
  file_names = open('exercicio06/nomes.txt', 'r')
  names_list = file_names.readlines()
  file_names.close()

  ##Formar uma lista com todas as notas
  notas_list = []
  file_notas = open('exercicio06/notas.txt', 'r')
  for n in file_notas:
    notas_list.append(n)
  file_notas.close()

  media_alunos = []
  for aluno in range(len(names_list)):
    notas_list[aluno] = notas_list[aluno].split(" ")
    if "\n" in notas_list[aluno]:
      notas_list[aluno].remove("\n")

    aluno_media = 0
    t = 0
    for nota in notas_list[aluno]:
      t += 1
      aluno_media += float(nota)
    if t > total_notas:
      total_notas = t
    aluno_media = aluno_media / total_notas
    
    names_list[aluno] = names_list[aluno].split("\n")
    ###Adicionando na lista de media dos alunos em geral
    media_alunos.append(f"{names_list[aluno][0]} media: {aluno_media} \n")

  ##criando o arquivo com o nome dos alunos e suas respectivas medias
  file_media = open('exercicio06/media_alunos.txt', 'w')
  file_media.writelines(media_alunos)    
  file_media.close()

def main():
  media("nomes.txt", "notas.txt")
main()
