import random
import module_utilits

def sortear_palavras(total_words):
   """Função que sortei as palavras de acordo com o modo de jogo(uma palavra, dueto, quarteto)."""
   ##Sortear as palavras, verificando se alguma ja foi utilizada
   file_words = open('arquivos/words.txt', 'r')
   file_used_words = open('arquivos/words_usadas.txt', 'r')
   list_used_words = file_used_words.readlines()
   list_words = file_words.readlines()
   file_words.close()
   file_used_words.close()
   drawn_words = []
   
   ##Sortear o total de palavras de acordo com o modo de jogo e guardar em uma lista.
   while len(drawn_words) != total_words:
      if (len(list_words) - len(list_used_words)) < total_words:
         return False
      word = list_words[random.randint(0, len(list_words) - 1)].upper()

      if word not in list_used_words:
         word = word.replace("\n", "")
         
         if word not in drawn_words and len(word) == 5:
            drawn_words.append(word)
      
   return drawn_words

def input_word_tentativa(words_usadas):
   """Função que pede ao jogador a palavra tentativa e verifica se ela já foi utilizada, 
      se tem 5 letras e sem não tem números nem espaços em branco."""
   ####Realizar o imput ao jogador respeitando as regras.
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

def colorir_palavras(attempts, green_letters, yellow_letters, colorful_tried_words, word, palavra_tentativa, drawn_words):
   """Função que adiciona cor as letras e guarda as tentativas em uma lista dentro de uma lista."""
   ##Criar duas listas com o dicionario, uma com os indices das letras e outra com as letras.
   list_green_letters = list(green_letters.values())
   list_indices_letters_green = list(green_letters.keys())
   
   for i in range(5):
      ##For com contagem ate 5 para ordenar a palavra tentada em uma variavel colorida
      if i in list_indices_letters_green:
         colored_letter = f"\033[32m{palavra_tentativa[i]}\033[0m"
         colorful_tried_words[attempts][word] = f"{colorful_tried_words[attempts][word]}{colored_letter} | "
      
      ###Se o total de tal letra na palavra sorteada for igual ao total dessa letra que ja esta em cor verde 
      ##se essa mesma letra aparecer novamente na palavra tentativa ela não irá ficar amarela.
      elif i in yellow_letters and list_green_letters.count(palavra_tentativa[i]) != drawn_words[word].count(palavra_tentativa[i]):
         colored_letter = f"\033[33m{palavra_tentativa[i]}\033[0m"
         colorful_tried_words[attempts][word] = f"{colorful_tried_words[attempts][word]}{colored_letter} | "

      else:
         colorful_tried_words[attempts][word] = f"{colorful_tried_words[attempts][word]}{palavra_tentativa[i]} | "
   return colorful_tried_words

def game(total_words):
   """Função principal que rodo o jogo, chamando outras funções 
      e separando as letras corretas ou em posições erradas."""
   drawn_words = sortear_palavras(total_words)

   if drawn_words == False:
      print("QUANTIDADE DE PALAVRAS INSUFICIENTES!")
      return
   
   ##Criando um modo de conferir se o jogador acertou alguma palavra, juntamente com um contador e uma lista para guardar as palavras tentadas
   colorful_tried_words = []
   attempts = 0
   successful_check = []
   record_words_used = []
   for i in range(total_words):
      successful_check.append(False)
      
   ###Tentativas do jogador, conferindo as letras das palavras 
   while True:
      print(drawn_words)
      colorful_tried_words.append([])
      word_try, record_words_used = input_word_tentativa(record_words_used)
      module_utilits.clear_terminal()
      
      for word in range(len(drawn_words)):
         colorful_tried_words[attempts].append("")
         green_letters = {}
         yellow_letters = []
         if successful_check[word] == True:
            colorful_tried_words[attempts][word] = colorful_tried_words[attempts-1][word]
         else:
            for letter in range(len(drawn_words[word])):
               if word_try[letter] == drawn_words[word][letter]:
                  green_letters[letter] = word_try[letter]

               elif word_try[letter] in drawn_words[word]:
                  yellow_letters.append(letter)
               
               if word_try == drawn_words[word]:
                  successful_check[word] = True
         
            colorful_tried_words = colorir_palavras(attempts, green_letters, yellow_letters, colorful_tried_words, word, word_try, drawn_words)
      
      space = " " * 10
      for i in range(len(colorful_tried_words)):
         if len(drawn_words) == 4:
            print(colorful_tried_words[i][0], space, colorful_tried_words[i][1], space, colorful_tried_words[i][2], space, colorful_tried_words[i][3])
      
         elif len(drawn_words) == 2:
            print(colorful_tried_words[i][0], space, colorful_tried_words[i][1])

         else:
            print(colorful_tried_words[i][0])
      attempts += 1

      if len(drawn_words) == 4 and attempts == 8 or len(drawn_words) == 2 and attempts == 6 or len(drawn_words) == 1 and attempts == 5:
         print("\n[LOSS] Você perdeu, suas tentativas acabaram. Melhor sorte na próxima vez.")
         confirm = input("::PRECIONE ENTER PARA VOLTAR AO MENU::")
         break
      
      if len(drawn_words) == successful_check.count(True):
         print("\n[WIN] Parabéns! Você venceu o jogo!")
         confirm = input("::PRECIONE ENTER PARA VOLTAR AO MENU::")
         folder_words_used = open('arquivos/words_usadas.txt', 'a')
         for word_used in drawn_words:
            folder_words_used.write(word_used)
            folder_words_used.write("\n")
         folder_words_used.close()
         break 
