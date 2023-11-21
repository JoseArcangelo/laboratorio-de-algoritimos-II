def reset_wrods_used():
  """Função que redefini as palavras já utlizadas, deixando disponiveis para aparecer novamente."""
  file = open('arquivos/words_usadas.txt', 'w')
  l = []
  file.writelines(l)
  file.close()
  print("::O GAME FOI RESETADO, AS PALAVRAS JÁ USADAS ESTÃO DISPONÍVEIS NOVAMENTE!::")
