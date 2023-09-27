import module_stock
import module_sales
import module_historic
import module_menu
import os

def clear_terminal():
    if os.name == 'posix': 
        return os.system('clear')  
    elif os.name == 'nt': 
        return os.system('cls') 

def main():
    print("---< GESTÃO DE ESTOQUE MERCADINHO DO BRIAN >---")
    stock = {"chinelo": {"amount": 40, "price_historic": [5], "category": "roupas"}}
    sales_record = []
    historical_changes = []

    while True:
        option = module_menu.menu()

        if option == "1":
            clear_terminal()
            stock, historical_changes = module_stock.add_product(stock, historical_changes)

        elif option == "2":
            clear_terminal()
            module_stock.search_product(stock, sales_record)
            
        elif option == "3":
            clear_terminal()
            module_stock.show_products(stock)

        elif option == "4":
            clear_terminal()
            stock, sales_record = module_sales.sell_produts(stock, sales_record)

        elif option == "5":
            clear_terminal()
            module_historic.sales(sales_record)

        elif option == "6":
            clear_terminal()
            stock, historical_changes = module_stock.delete_product(stock, historical_changes)

        elif option == "7":
            clear_terminal()
            stock, historical_changes = module_stock.change_product_value(stock, historical_changes)

        elif option == "8":
            clear_terminal()
            module_stock.view_by_category(stock)

        elif option == "9":
            clear_terminal()
            module_historic.see_historical_change(historical_changes)

        elif option == "10":
            clear_terminal()
            print("É O BRAIAN !!!! ZUMMM")
            print("Saindo...")
            break

        else:
            print("--OPÇÃO INVÁLIDA!!!--")
        
main()
