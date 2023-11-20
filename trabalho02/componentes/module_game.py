import random
import module_utilits

def sortear_palavras(total_words):
   ##Sortear as palavras, verificando se alguma ja foi utilizada
   folder_words = open('arquivos/words.txt', 'r')
   folder_words_usadas = open('arquivos/words_usadas.txt', 'r')
   list_words_usadas = folder_words_usadas.readlines()
   list_words = folder_words.readlines()
   folder_words.close()
   folder_words_usadas.close()
   palavras_sorteadas = []

   if (len(list_words) - len(list_words_usadas)) < total_words:
      return False
   
   while True:
      word = list_words[random.randint(0, len(list_words) - 1)].upper()
      
      if word not in list_words_usadas:
         word = word.replace("\n", "")
         
         if word not in palavras_sorteadas and len(word) == 5:
            palavras_sorteadas.append(word)
         
      if len(palavras_sorteadas) == total_words:
         break

   return palavras_sorteadas

def input_word_tentativa(words_usadas):
   while True:
      try:
         word = input("\nInforme uma palavra: ").upper()
         if len(word) != 5:
            raise NameError("[ERRO] VOCÊ INFORMOU UMA PALAVRA QUE NÃO POSSUI 5 LETRAS! ")
         if not word.isalpha():
            raise NameError("[ERRO] NÃO É PERMITIDO NÚMEROS NEM ESPAÇOS EM BRANCO!")
         if word in words_usadas:
            raise NameError("VOCÊ JÁ UTILIZOU ESTA PALAVRA!")
         else:
            words_usadas.append(word)
            return word, words_usadas
      except ValueError:
         print("[ERRO] VOCÊ INFORMOU UMA PALAVRA INVÁLIDA!")
      except NameError as e:
         print(e)

def colorir_palavras(round, letras_verdes, letras_amarelas, historico_palavras_tentadas, palavra, palavra_tentativa , palavras_sorteadas):
   lista_letras_verdes = list(letras_verdes.values())
   lista_indices_verdes = list(letras_verdes.keys()) 
   for i in range(5):

      if i in lista_indices_verdes:
         colored_letter = f"\033[32m{palavra_tentativa[i]}\033[0m"
         historico_palavras_tentadas[round][palavra] = f"{historico_palavras_tentadas[round][palavra]}{colored_letter} | "
      
      elif i in letras_amarelas and lista_letras_verdes.count(palavra_tentativa[i]) != palavras_sorteadas[palavra].count(palavra_tentativa[i]):
         colored_letter = f"\033[33m{palavra_tentativa[i]}\033[0m"
         historico_palavras_tentadas[round][palavra] = f"{historico_palavras_tentadas[round][palavra]}{colored_letter} | "
     
      else:
         historico_palavras_tentadas[round][palavra] = f"{historico_palavras_tentadas[round][palavra]}{palavra_tentativa[i]} | "
   return historico_palavras_tentadas

def game(total_words):
   ##Sortear as palavras, verificando se alguma ja foi utilizada
   palavras_sorteadas = sortear_palavras(total_words)
   if palavras_sorteadas == False:
      print("QUANTIDADE DE PALAVRAS INSUFICIENTES!")
      return
   
   ##Criando um modo de conferir se o jogador acertou alguma palavra, juntamente com um contador e uma lista para guardar as palavras tentadas
   historico_palavras_tentadas = []
   round = 0
   acertos = []
   words_usadas = []
   for i in range(total_words):
      acertos.append(False)
      
  ###Tentativas do jogador, conferindo se as letras das palavras
   while True:
      print(palavras_sorteadas)
      historico_palavras_tentadas.append([])
      palavra_tentativa, words_usadas = input_word_tentativa(words_usadas)
      module_utilits.clear_terminal()
      
      for palavra in range(len(palavras_sorteadas)):
         historico_palavras_tentadas[round].append("")
         letras_verdes = {}
         letras_amarelas = []
         if acertos[palavra] == True:
            historico_palavras_tentadas[round][palavra] = historico_palavras_tentadas[round-1][palavra]
         else:
            for letra in range(len(palavras_sorteadas[palavra])):
               if palavra_tentativa[letra] == palavras_sorteadas[palavra][letra]:
                  letras_verdes[letra] = palavra_tentativa[letra]

               elif palavra_tentativa[letra] in palavras_sorteadas[palavra]:
                  letras_amarelas.append(letra)
               
               if palavra_tentativa == palavras_sorteadas[palavra]:
                  acertos[palavra] = True
         
            historico_palavras_tentadas = colorir_palavras(round, letras_verdes, letras_amarelas, historico_palavras_tentadas, palavra, palavra_tentativa, palavras_sorteadas)
      
      for i in range(len(historico_palavras_tentadas)):
         if len(palavras_sorteadas) == 4:
            print(historico_palavras_tentadas[i][0], historico_palavras_tentadas[i][1], historico_palavras_tentadas[i][2], historico_palavras_tentadas[i][3])
      
         elif len(palavras_sorteadas) == 2:
            print(historico_palavras_tentadas[i][0], historico_palavras_tentadas[i][1])

         else:
            print(historico_palavras_tentadas[i][0])
      round += 1

      if len(palavras_sorteadas) == 4 and round == 8 or len(palavras_sorteadas) == 2 and round == 6 or len(palavras_sorteadas) == 1 and round == 5:
         print("[LOSS] VOCÊ PERDEU!")
         confirm = input("::PRECIONE ENTER PARA VOLTAR AO MENU::")
         break
      
      if len(palavras_sorteadas) == acertos.count(True):
         print("[WIN] VOCÊ VENCEU O JOGO!")
         confirm = input("::PRECIONE ENTER PARA VOLTAR AO MENU::")
         folder_words_usadas = open('arquivos/words_usadas.txt', 'a')
         for word_usada in palavras_sorteadas:
            folder_words_usadas.write(word_usada)
            folder_words_usadas.write("\n")
         folder_words_usadas.close()
         break
