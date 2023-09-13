def menu():
    print("\n1 - Adicionar um produto")
    print("2 - Buscar um produto")
    print("3 - Visualizar todos os produtos")
    print("4 - Vender um produto")
    print("5 - Relatorio de vendas")
    print("6 - Sair")
    option = input("Informe a opcao desejada: ")
    return option

def add_product(my_products):
    print("\n --ADICIONAR PRODUTO--")
    name = input("Informe o nome do produto: ")
    amount = int(input(f"Informe a quantidade que deseja adicionar ao estoque de {name}: "))

    if name in my_products:
        my_products[name]["amount"] += amount

    else:
        my_products[name] = {
            "amount": amount,
            "price": float(input(f"Informe o preço unitário do produto {name}: "))
        }

    print("--PRODUTO ADICIONADO!--")
    return my_products

def search_product(my_products):
    print("\n--BUSCAR PRODUTO--")
    name = input("Informe o nome do produto que deseja encontrar: ")
    if name in my_products:
        print(f"Informações do produto --> Nome: {name} - Estoque: {my_products[name]['amount']} unidades - Preço: R$ {my_products[name]['price']}")

    else:
        print("--ESTE PRODUTO NÃO CONSTA EM NOSSO SISTEMA!--")

def show_products(my_products):
    print("\n----LISTA DE PRODUTOS----")
    for product in my_products:
        print(f"--> Produto: {product} - Quantidade em estoque: {my_products[product]['amount']} unidades - Preço: R$ {my_products[product]['price']}")

def sell_produts(my_products, sales_record):
    print("\n----VENDER PRODUTO----")

    name = input("Informe o nome do produto vendido: ")
    if name in my_products:
        quantity_sell = int(input(f"Informe a quantidade de {name} vendidos: "))

        if quantity_sell > my_products[name]["amount"]:
            print("NOSSO ESTOQUE É INFERIOR A QUANTIDADE QUE DESEJA VENDER!")

        else:
            my_products[name]["amount"] -= quantity_sell
            profit_sale = quantity_sell * my_products[name]["price"]
            print("Valor total da venda: R$", profit_sale)

            if name not in sales_record:
                sales_record[name] = {
                    "value_total_sale": profit_sale,
                    "amount": quantity_sell
                }

            else:
                sales_record[name]["value_total_sale"] += profit_sale
                sales_record[name]["amount"] += quantity_sell

            if my_products[name]["amount"] == 0:
                my_products.pop(name)

    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")

    return my_products, sales_record

def sales(sales_record):
    print("\n--RELATÓRIO DE VENDAS--")
    for product in sales_record:
        print(f"--> Nome do produto: {product} - Quantidade vendida: {sales_record[product]['amount']} unidade - Lucro total: R$ {sales_record[product]['value_total_sale']}")

def main():
    print("---<MERCADINHO DO PILÉCO>---")
    my_products = {}
    sales_record = {}

    while True:
        option = menu()
        if option == "1":
            my_products = add_product(my_products)

        elif option == "2":
            search_product(my_products)

        elif option == "3":
            show_products(my_products)

        elif option == "4":
            my_products, sales_record = sell_produts(my_products, sales_record)

        elif option == "5":
            sales(sales_record)

        elif option == "6":
            print("VOLTE SEMPRE AO MERCADINHO DO PILÉCO!!")
            print("Saindo...")
            break

        else:
            print("--OPÇÃO INVÁLIDA!!!--")

main()
