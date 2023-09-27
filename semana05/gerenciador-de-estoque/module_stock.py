import datetime

def add_product(stock, historical_changes):
    """Função que adiciona um produto no estoque, ela tem com parametros
    o estoque e o historico de alterações."""

    print("\n --ADICIONAR PRODUTO--")
    name_product = input("Informe o nome do produto: ")
    amount = int(input(f"Informe a quantidade que deseja adicionar ao estoque de {name_product}: "))
    date_now = datetime.datetime.now()
    date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min"
    if name_product in stock:
        stock[name_product]["amount"] += amount
        historical_changes.append(f"Foi adicionado {amount} unidades ao estoque de {name_product} DATA: {date_now}")

    else:
        price = float(input(f"Informe o preço unitário de {name_product}: "))
        stock[name_product] = {
            "amount": amount,
            "price": price,
            "price_historic": [price],
            "category": input(f"Informe a categoria de {name_product}: "),}
        historical_changes.append(f"O produto {name_product} foi adicionado ao estoque com {amount} unidades - DATA: {date_now}")

    print("--PRODUTO ADICIONADO!--")
    
    return stock, historical_changes

def search_product(stock, sales_record):
    """Função que busca um produto no estoque e seu histórico de vendas, 
    ela tem como parâmetros o estoque e o histórico de vendas."""

    print("\n--BUSCAR PRODUTO--")
    name_product = input("Informe o nome do produto que deseja encontrar: ")
    if name_product in stock:
        print(f"Informações de {name_product}")
        print(f"Quantidade em estoque: {stock[name_product]['amount']} unidadeas")
        print(f"Preço unitário: R$ {stock[name_product]['price_historic'][-1]}")
        print(f"Categoria: {stock[name_product]['category']}")

        print(f"\nHistorico de vendas de {name_product}:")
        def sale_in_sales_record(sales_record):
            return name_product in sales_record
        
        sale = filter(sale_in_sales_record, sales_record)

        verification = False
        for item in sale:
            verification = True
            print(item)
            
        if verification == False:
            print(f"Nenhuma venda de {name_product} foi realizada!")
    else:
        print("--ESTE PRODUTO NÃO CONSTA EM NOSSO SISTEMA!--")


def show_products(stock):
    """Função que lista todos os produtos que estão no estoque,
    ela recebe como parâmetros o estoque."""

    print("\n----LISTA DE PRODUTOS----")
    if len(stock) == 0:
        print("OPS! O estoque está vazio!")

    else:
        for product in stock:
            print(f"--> Produto: {product} - Quantidade em estoque: {stock[product]['amount']} unidades - Preço: R$ {stock[product]['price_historic'][-1]} - Categoria: {stock[product]['category']}")

def delete_product(stock, historical_changes):
    """Função que remove um produto do estoque, salvando esta mudança no histórico de alterações,
    ela recebe como parâmetros o estoque e o histórico de alterações."""

    print("\n --EXCLUIR PRODUTO--")
    name_product = input("Informe o nome do produto que deseja remover de seu estoque: ")
    if name_product in stock:
        stock.pop(name_product)
        print(f"{name_product} foi removido com sucesso!")
        date_now = datetime.datetime.now()
        date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min"
        historical_changes.append(f"O produto {name_product} foi removido do stock - DATA: {date_now}")
    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")
    return stock, historical_changes

def change_product_value(stock, historical_changes):
    """Função que atualiza o valor do de um produto deixando salvo esta mudança
    no historico de alterações, ela recebe como parâmetros o estoque e o histórico
    de alterações."""

    print("\n--ALTERAR VALOR DE UM PRODUTO--")
    name_product = input("Informe o nome do produto que deseja alterar o valor: ")
    if name_product in stock:
        new_value = float(input(f"Informe o valor atualizado de {name_product}: "))
        date_now = datetime.datetime.now()
        date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min"
        historical_changes.append(f"O preço unitáro de {name_product} que era R$ {stock[name_product]['price_historic'][-1]} for alterado para R$ {new_value} data: {date_now} ")
        stock[name_product]["price_historic"].append(new_value)
        stock[name_product]["price"] = new_value
        print("O PREÇO DO PRODUTO FOI ALTERADO!")

    else:
        print("OPS! O ESTOQUE NÂO POSSUI O PRODUTO INFORMADO!")
    return stock, historical_changes

def view_by_category(stock):
    """Função que lista todos os itens que pertecem a uma mesma categoria, 
    ela recebe como parametro o estoque."""

    print("\n--VISUALIZAR PRODUTOS POR CATEGORIA--")
    name_category = input("Informe o nome da categoria do produto: ")
    verification = False
    for product in stock:
        if stock[product]["category"] == name_category:
            print(f"Nome do produto: {product} - Quantidade em estoque: {stock[product]['amount']} - Preço unitário: R$ {stock[product]['price_historic'][-1]}")
            verification = True
    if verification == False:
        print("OPS! O ESTOQUE NÃO POSSUI NENHUM PRODUTO COM ESSA CATEGORIA!")
