import datetime
def add_product(stock, historical_changes):
    print("\n --ADICIONAR PRODUTO--")
    name = input("Informe o nome do produto: ")
    amount = int(
        input(f"Informe a quantidade que deseja adicionar ao estoque de {name}: "))
    if name in stock:
        stock[name]["amount"] += amount
        historical_changes.append(f"Foi adicionado {amount} unidades ao estoque de {name}")
    else:
        price = float(input(f"Informe o preço unitário de {name}: "))
        stock[name] = {
            "amount": amount,
            "price": price,
            "price_historic": [price],
            "category": input(f"Informe a categoria de {name}: "),}
    print("--PRODUTO ADICIONADO!--")
    return stock, historical_changes

def search_product(stock, sales_record):
    print("\n--BUSCAR PRODUTO--")
    name_product = input("Informe o nome do produto que deseja encontrar: ")
    if name_product in stock:
        print(f"Informações de {name_product}")
        print(f"Quantidade em estoque: {stock[name_product]['amount']} unidadeas")
        print(f"Preço unitário: R$ {stock[name_product]['price_historic'][-1]}")
        print(f"Categoria: {stock[name_product]['category']}")
        print(f"Historico de vendas de {name_product}:")
        for sale in sales_record:
            if name_product in sale:
                print(sale)
    else:
        print("--ESTE PRODUTO NÃO CONSTA EM NOSSO SISTEMA!--")

def show_products(stock):
    print("\n----LISTA DE PRODUTOS----")
    for product in stock:
        print(f"--> Produto: {product} - Quantidade em estoque: {stock[product]['amount']} unidades - Preço: R$ {stock[product]['price_historic'][-1]} - Categoria: {stock[product]['category']}")

def delete_product(stock, historical_changes):
    print("\n --ECLUIR PRODUTO--")
    name = input("Informe o nome do produto que deseja remover de seu estoque: ")
    if name in stock:
        stock.pop(name)
        print(f"{name} foi removido com sucesso!")
        date_now = datetime.datetime.now()
        date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min e {date_now.second} seg"
        historical_changes.append(f"O produto {name} foi removido do stock - DATA: {date_now}")
    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")
    return stock, historical_changes

def change_product_value(stock, historical_changes):
    print("\n--ALTERAR VALOR DE UM PRODUTO--")
    name = input("Informe o nome do produto que deseja alterar o valor: ")
    if name in stock:
        new_value = float(input(f"Informe o valor atualizado de {name}: "))
        date_now = datetime.datetime.now()
        date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min"
        historical_changes.append(f"O preço unitáro de {name} que era R$ {stock[name]['price_historic'][-1]} for alterado para R$ {new_value} data: {date_now} ")
        stock[name]["price_historic"].append(new_value)
        stock[name]["price"] = new_value
        print("O PREÇO DO PRODUTO FOI ALTERADO!")

    else:
        print("OPS! O STOCK NÂO POSSUI O PRODUTO INFORMADO!")
    return stock, historical_changes

def view_by_category(stock):
    print("\n--VISUALIZAR PRODUTOS POR CATEGORIA--")
    name_category = input("Informe o nome da categoria do produto: ")
    for product in stock:
        if stock[product]["category"] == name_category:
            print(f"Nome do produto: {product} - Quantidade em estoque: {stock[product]['amount']} - Preço unitário: R$ {stock[product]['price_historic'][-1]}")
    if name_category not in stock[product]["category"]:
        print("OPS! O ESTOQUE NÃO POSSUI NENHUM PRODUTO COM ESSA CATEGORIA!")
