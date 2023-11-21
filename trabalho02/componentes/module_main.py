import module_menu
import module_utilits
import module_game
import module_reset_words_used

def main():
   """Função principal do código que chama os outros módulos"""
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
         module_utilits.clear_terminal()
         module_reset_words_used.reset_wrods_used()

      elif option == "5":
         print("SAINDO...")
         break
      
      else:
         print("::OPÇÃO INVÁLIDA!::")
main()  
