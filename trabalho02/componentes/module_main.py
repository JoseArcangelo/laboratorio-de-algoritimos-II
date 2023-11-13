import module_menu
import module_utilits
import module_game

def main():
    """Função principal do código que chama os outros módulos"""
    print(":::BEM VINDO AO JOGO TERMO!:::")
    while True: 
      option = module_menu.menu()
      if option == "1":
         module_utilits.clear_terminal()
         module_game.game(1)
      elif option == "2":
         module_utilits.clear_terminal()
         module_game.game(2)

      elif option == "3":
         module_utilits.clear_terminal()
         module_game.game(4)

      elif option == "4":
         print("SAINDO...")
         break
         
main()  
