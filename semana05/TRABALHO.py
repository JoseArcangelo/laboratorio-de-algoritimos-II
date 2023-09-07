def menu():
    print("1 - Adicionar um produto")
    print("2 - Buscar um produto")
    print("3 - Visualizar todos os produtos")
    print("4 - Vender um produto")
    print("5 - Relatorio de vendas")
    print("6 - Sair")
    option = int(input("Informe a opcao desejada: "))
    return option

def add_product(products):
    name = input("Informe o nome do produto: ")
    amount = int(input(f"Informe a quantidade que deseja adicionar ao estoque de {name}: "))
    if name in products:
        products[name]["amount"] += amount
        
    else:
        description = {}
        description["amount"] = amount
        description["price"] = float(input(f"Informe o preço unitário do produto {name}: "))
        products[name] = description
    print("--PRODUTO ADICIONADO E INCLUIDO NO ESTOQUE!--")
    return products

def search_product(products):
    print("\n--BUSCAR PRODUTO--")
    name = input("Informe o nome do produto que deseja encontrar: ")
    if name in products:
        print(f"Informações do produto --> Nome: {name} - Estoque: {products[name].get('amount')} unidades - Preço: R$ {products[name].get('price')} \n")
    
    else:
        print("--ESTE PRODUTO NÃO CONSTA EM NOSSO SISTEMA!--")

def show_products(products):
    print("\n----LISTA DE PRODUTOS----")
    for product in products:
        print(f"->Produto:{product} Quantidade em estoque: {products[product].get('amount')} unidades - Preço: R$ {products[product].get('price')}\n")


def sell_produts(products, sales_record):
    print("\n----VENDER PRODUTO----")
    
    name = input("Informe o nome do produto vendido: ")
    if name in products:
        quantity_sell = int(input(f"Informe a quantidade de {name} vendidos: "))

        if quantity_sell > products[name].get('amount'):
            print("NOSSO ESTOQUE É INFERIOR A QUANTIDADE QUE DESEJA VENDEER!")
        
        else:
            products[name]["amount"] -= quantity_sell
            lucro = quantity_sell * products[name]["price"]
            if name not in sales_record:
                detals = {}
                detals["lucro"] = lucro
                detals["amount"] = quantity_sell
                sales_record[name] = detals
                
    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")
        
    return products, sales_record
        

def main():
    print("---<BEM VINDO AO MERCADINHO DO PILÉCO>---")
    products = {}
    sales_record = {}

    while True:
        option = menu()
        if option == 1:
            add_product(products)

        elif option == 2:
            search_product(products)

        elif option == 3:
            show_products(products)
        
        elif option == 4:
            sell_produts(products, sales_record)
            print(sales_record, products)
            
main()
