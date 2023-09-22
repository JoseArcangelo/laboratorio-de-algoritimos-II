import datetime
def menu():
    print("\n---> MENU <---")
    print("1 - Adicionar um produto")
    print("2 - Buscar um produto")
    print("3 - Visualizar todos os produtos")
    print("4 - Vender um produto")
    print("5 - Relatorio de vendas")
    print("6 - Excluir produto")
    print("7 - Alterar valor de um produto")
    print("8 - Visualizar po categoria")
    print("9 - Sair")
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
            "price_historic": [float(input(f"Informe o preço unitário do produto {name}: "))],
            "category": input(f"Informe a categoria de {name}: ")
        }

    print("--PRODUTO ADICIONADO!--")
    return my_products

def search_product(my_products, sales_record):
    print("\n--BUSCAR PRODUTO--")
    name = input("Informe o nome do produto que deseja encontrar: ")
    if name in my_products:
        print(f"Informações de {name}")
        print(f"Quantidade em estoque: {my_products[name]['amount']} unidadeas")
        print(f"Preço unitário: R$ {my_products[name]['price_historic'][-1]}")
        print(f"Categoria: {my_products[name]['category']}")
        
        if name in sales_record:
            print(f"Histórico de vendas de {name}:")
            for sale in sales_record:
                print(f"Data: {sales_record[sale]['date']}, Quantidade vendida: {sales_record[sale]['amount']}, Valor total: R$ {sales_record[sale]['value_total_sale']}")
        
    else:
        print("--ESTE PRODUTO NÃO CONSTA EM NOSSO SISTEMA!--")

def show_products(my_products):
    print("\n----LISTA DE PRODUTOS----")
    for product in my_products:
        print(f"--> Produto: {product} - Quantidade em estoque: {my_products[product]['amount']} unidades - Preço: R$ {my_products[product]['price_historic'][-1]} - Categoria: {my_products[product]['category']}")
        
def sell_produts(my_products, sales_record):
    print("\n----VENDER PRODUTO----")

    name = input("Informe o nome do produto vendido: ")
    if name in my_products:
        quantity_sell = int(input(f"Informe a quantidade de {name} vendidos: "))

        if quantity_sell > my_products[name]["amount"]:
            print("NOSSO ESTOQUE É INFERIOR A QUANTIDADE QUE DESEJA VENDER!")

        else:
            my_products[name]["amount"] -= quantity_sell
            profit_sale = quantity_sell * my_products[name]["price_historic"][-1]
            print("Valor total da venda: R$", profit_sale)

            if name not in sales_record:
                date_now = datetime.datetime.now()
                sales_record[name] = {
                    "value_total_sale": profit_sale,
                    "amount": quantity_sell,
                    "date": f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas e {date_now.minute} minutos"
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
        print(f"--> Nome do produto: {product} - Quantidade vendida: {sales_record[product]['amount']} unidade - Lucro total: R$ {sales_record[product]['value_total_sale']} - Data da venda: {sales_record[product]['date']}")
        
def delete_product(my_products):
    name = input("Informe o nome do produto que deseja remover de seu estoque: ")
    if name in my_products:
        my_products.pop(name)
        print(f"{name} foi removido com sucesso!")
        return my_products
    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")
        
def change_product_value(my_products):
    name = input("Informe o nome do produto que deseja alterar o valor: ")
    if name in my_products:
        new_value = float(input(f"Informe o valor atualizado de {name}: "))
        my_products[name]['price_historic'].append(new_value)
        return my_products
        
def view_by_category(my_products):
    name_category = input("Informe o nome da categoria do produto: ")
    for product in my_products:
        if my_products[product]["category"] == name_category:
            print(f"Nome: {product} - Quantidade em estoque: {my_products[product]['amount']} unidades - Preço: R$ {my_products[product]['price'][-1]}")

def main():
    print("---<GESTÃO DE ESTOQUE MERCADINHO DO BRIAN>---")
    my_products = {
        "chinelo":
            {"amount": 40,
            "price_historic": [5],
            "category": "roupas"}}
    sales_record = {}
    
    while True:
        option = menu()
        if option == "1":
            my_products = add_product(my_products)

        elif option == "2":
            search_product(my_products, sales_record)

        elif option == "3":
            show_products(my_products)

        elif option == "4":
            my_products, sales_record = sell_produts(my_products, sales_record)

        elif option == "5":
            sales(sales_record)
            
        elif option == "6":
            my_products = delete_product(my_products)
            
        elif option == "7":
            my_products = change_product_value(my_products)
            print(my_products)
        
        elif option == "8":
            view_by_category(my_products)
        
        elif option == "9":
            print("É O BRAIAN !!!! ZUMMM")
            print("Saindo...")
            break

        else:
            print("--OPÇÃO INVÁLIDA!!!--")

main()
