<h1 align="center">Trabalho Avaliativo G2  S2</h1>
<h1 align="center">Sistemas de informação - Laboratório de Algoritmos II</h1>
<h1 align="center">AMF</h1>

<p align="center">
  <img  src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
</p>

<h1 align="center">T | E | R | M | O</h1>

<p>Este é um programa Python que recria o clássico jogo Termo, desafiando os jogadores a adivinharem palavras de 5 letras. O jogo oferece três modos de dificuldade, o modo de adivinhação de uma palavra, o de adivinhação de duas palavras e o de adivinhação de quatro palavras.</p>

<h2 align="justify">Funcionalidades</h2>

<p>O jogo possui um menu que contém as seguintes opções: </p>

<h3 align="justify">1.  MODO DE ADIVINHAÇÃO DE UMA PALAVRA</h3>
<p>O jogador escolhe este modo e tenta adivinhar uma palavra secreta de 5 letras gerada aleatoriamente pelo programa em até 5 tentativas. Caso o jogador acerte essapalavra ela nao aparecerá no jogo posteriormente em outra partida.</p>

<h3 align="justify">2. MODO DUETO</h3>
<p>O jogador precisa adivinhar duas palavras distintas em até 6 tentativas, ambas com 5 letras. Caso o jogador acerte essas palavras elas n]ao apareceram novamente em outra partida.</p>

<h3 align="justify">3. MODO QUARTETO</h3>
<p> O jogador enfrenta a tarefa de decifrar quatro palavras de 5 letras cada em até 8 tentativas. Caso o jogador acerte estas palavras elas não apereceram novamente em outra partida.</p>

<h3 align="justify">4. REDEFINIR PALAVRAS JÁ USADAS</h3>
<p>Ao executar essa opção as palavras que foram usadas anteriormente poderam ser usadas novamente.</p>

<h3 align="justify">5. SAIR</h3>
<p>O jogo é finalizado.</p>

<h2 align="justify">COMO JOGAR</h2>
<p>O jogo oferece três modos de dificuldade, cada um com suas próprias características:</p>

<h3 align="justify">_Modo de Adivinhação de Uma Palavra: </h3>
<p> Neste modo, o jogador tem 5 tentativas para adivinhar uma palavra secreta de 5 letras gerada aleatoriamente pelo programa. Após cada tentativa, o jogador recebe feedback visual:</p>
<p> - Letras corretas e na posição correta são destacadas em verde.</p>
<p> - Letras corretas, mas em posições erradas, são destacadas em amarelo.</p>
<p> - Caso a letra não esteja na palavra sorteada, ela permanecerá em branco.</p>

<h3 align="justify">_Modo de Adivinhação de Duas Palavras:  </h3>
<p>  A dificuldade aumenta, e o jogador tem 6 tentativas para adivinhar duas palavras distintas, ambas com 5 letras. O feedback visual é fornecido da mesma forma que no Modo de Uma Palavra.</p>

<h3 align="justify">_Modo de Adivinhação de Quatro Palavras: </h3>
<p> - O modo mais desafiador, no qual o jogador enfrenta a tarefa de decifrar quatro palavras de 5 letras cada. Aqui, são concedidas 8 tentativas, e o feedback detalhado ajuda o jogador a refinar suas estratégias de adivinhação.</p>

<h3 align="justify">Passo a passo para jogar:</h3>
<p>1. Execute o programa em Python.</p>
<p>2. Escolha o modo de dificuldade desejado.</p>
<p>3. Insira suas tentativas para adivinhar as palavras.</p>
<p>4. Receba feedback após cada tentativa, com destaque visual para letras corretas e suas posições.</p>
<p>5. Continue aprimorando suas estratégias dentro do limite de tentativas e divirta-se desvendando as palavras no Termo em Python!</p>

<h3 align="justify">Regras:</h3>
<p>1. Não é permitido números ao informar a palavra tentativa.</p>
<p>2. Não é permitido espaços em branco ao informar a palavra tentativa.</p>
<p>3. Não é permitido repetir palavras nas tentativas.</p>
<p>4. Ao escrever a palara tentativa ela deve conter 5 letras.</p>


<h2 align="justify">ARQUITETURA</h2>

<p> O sistema é dividido em módulos, modulo main sendo o arquivo central do sistema, e os outros 4 módulos: module_game, module_menu e module_utilits. Cada módulo possui um conjunto de funções. Também possui uma pasta com dois arquivos: words e words_usadas.</p>

<h3>module_menu</h3>
<p>Contém o menu de opções do sistema.</p>

<h3>module_game</h3>
<p>Contém mais a oarte funcional do game, onde são sorteadas as palavras, verificações de feedback e verificações de acerto.</p>

<h3>module_utilits</h3>
<p>Modulo que contém algumas funcionalidades uteis ao sistema de forma estética, como o de limpar o terminal.</p>

<h3>module_main</h3>
<p>Módulo central do sistema</p>

<h3>module_reset_words_used</h3>
<p>Comtém a função de redefinir as palavras já utilizadas.</p>

<h3>Arquivos</h3>
<p>na pasta arquivos contém o arquivo com as palavras que podem ser sorteadas e um outro arquivo com as palavras que já foram usadas.</p>

<h2 align="justify">AUTORES</h2>
<p>José Arcangelo de Souza Garlet</p>
<p>Lucas Descovi</p>
