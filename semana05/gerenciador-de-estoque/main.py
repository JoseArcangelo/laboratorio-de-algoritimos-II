import Stock
import Sales
import historic

def menu():
    print("\n---< MENU >---")
    print("1 - Adicionar um produto")
    print("2 - Buscar um produto")
    print("3 - Visualizar todos os produtos")
    print("4 - Vender um produto")
    print("5 - Relatorio de vendas")
    print("6 - Excluir produto")
    print("7 - Alterar valor de um produto")
    print("8 - Visualizar po categoria")
    print("9 - Visualizar historico de alterações")
    print("10 - Sair")
    option = input("Informe a opcao desejada: ")
    return option

def main():
    print("---< GESTÃO DE ESTOQUE MERCADINHO DO BRIAN >---")
    stock = {"chinelo": {"amount": 40, "price_historic": [5], "category": "roupas"}}
    sales_record = []
    historical_changes = []

    while True:
        option = menu()

        if option == "1":
            stock, historical_changes = Stock.add_product(stock, historical_changes)

        elif option == "2":
            Stock.search_product(stock, sales_record)

        elif option == "3":
            Stock.show_products(stock)

        elif option == "4":
            stock, sales_record = Sales.sell_produts(stock, sales_record)

        elif option == "5":
            historic.sales(sales_record)

        elif option == "6":
            stock, historical_changes = Stock.delete_product(stock, historical_changes)

        elif option == "7":
            stock, historical_changes = Stock.change_product_value(stock, historical_changes)

        elif option == "8":
            Stock.view_by_category(stock)

        elif option == "9":
            historic.see_historical_change(historical_changes)

        elif option == "10":
            print("É O BRAIAN !!!! ZUMMM")
            print("Saindo...")
            break

        else:
            print("--OPÇÃO INVÁLIDA!!!--")

main()
