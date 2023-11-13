import random
import module_utilits

def game(total_words):
   ##Sortear as palavras, verificando se alguma ja foi utilizada
   folder_words = open('arquivos/words.txt', 'r')
   folder_words_usadas = open('arquivos/words_usadas.txt', 'r')
   list_words_usadas = folder_words_usadas.readlines()
   list_words = folder_words.readlines()
   palavras_sorteadas = []
   print(len(list_words))
   while True:
      word = list_words[random.randint(0, len(list_words) - 1)].upper()
      if word not in list_words_usadas:
         word = word.replace("\n", "")
         palavras_sorteadas.append(word)
         
      if len(palavras_sorteadas) == total_words:
         break
   folder_words.close()
   folder_words_usadas.close()
   
   ##Criando um modo de conferir se o jogador acertou alguma palavra, juntamente com um contador e uma lista para guardar as palavras tentadas
   historico_palavras_tentadas = []
   round = 0
   acertos = []
   for i in range(total_words):
      acertos.append(False)

   ###Tentativas do jogador, conferindo se as letras das palavras
   while True:
      print(palavras_sorteadas)
      historico_palavras_tentadas.append([])
      palavra_tentativa = str(input("\nInforme uma palavra: ")).upper()
      module_utilits.clear_terminal()

      for palavra in range(len(palavras_sorteadas)): 
         historico_palavras_tentadas[round].append("")
         if acertos[palavra] == True:
            historico_palavras_tentadas[round][palavra] = historico_palavras_tentadas[round - 1][palavra]
         
         else:
            for letra in range(len(palavra_tentativa)):
               if palavra_tentativa == palavras_sorteadas[palavra]:
                  acertos[palavra] = True
               
               if palavras_sorteadas[palavra][letra] == palavra_tentativa[letra]:               
                  colored_letter = f"\033[32m{palavra_tentativa[letra]}\033[0m"
                  historico_palavras_tentadas[round][palavra] = f"{historico_palavras_tentadas[round][palavra]}{colored_letter} | "
               elif palavra_tentativa[letra] in palavras_sorteadas[palavra]:
                  colored_letter = f"\033[33m{palavra_tentativa[letra]}\033[0m"
                  historico_palavras_tentadas[round][palavra] = f"{historico_palavras_tentadas[round][palavra]}{colored_letter} | "
               else:
                  historico_palavras_tentadas[round][palavra] = f"{historico_palavras_tentadas[round][palavra]}{palavra_tentativa[letra]} | "
         
      for i in range(len(historico_palavras_tentadas)):
         if len(palavras_sorteadas) == 4:
            print(historico_palavras_tentadas[i][0], historico_palavras_tentadas[i][1],  historico_palavras_tentadas[i][2], historico_palavras_tentadas[i][3])

         elif len(palavras_sorteadas) == 2:
            print(historico_palavras_tentadas[i][0], historico_palavras_tentadas[i][1])

         else:
            print(historico_palavras_tentadas[i][0])
      round += 1

      ###Verificando se o jogador nao tem mais tentativas
      if len(palavras_sorteadas) == 1 and round == 5 or len(palavras_sorteadas) == 2 and round == 6 or len(palavras_sorteadas) == 4 and round == 8:
         print(":::[GAME OVER!] VOCÊ PERDEU O JOGO!:::")
         confirm = input("\n:::PRECIONE ENTER PARA VOLTOU AO MENU:::")
         break
      
      ###Quando todas as palavras estao corretas, adicionando as palavras da partida no arquivo de palavras utilizadas
      print(acertos)
      if acertos.count(True) == len(acertos):
         print(":::[WIN] VOCÊ VENCEU O JOGO:::")
         file_words_usadas = open('arquivos/words_usadas.txt', 'a')
         for a in palavras_sorteadas:
            file_words_usadas.write(a)
            file_words_usadas.write("\n")   

         file_words_usadas.close()
         confirm = input("\n:::PRECIONE ENTER PARA VOLTOU AO MENU:::")
         break
               
