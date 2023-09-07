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
    description = {}
    description["amount"] = int(input(f"Informe a quantidade do estoque do produto {name}: "))
    description["price"] = float(input(f"Informe o preço unitário do produto {name}: "))
    products[name] = description
    return products

def search_product(products):
    name = input("Informe o nome do produto que deseja encontrar: ")
    if name in products:
        print(f"Informações do produto --> Estoque: {products[name].get('amount')} unidades - Preço: R$ {products[name].get('price')} \n")
    
    else:
        print("ESTE PRODUTO NÃO CONSTA EM NOSSO SISTEMA!")

def show_products(products):
    print("----LISTA DE PRODUTOS----")
    for product in products:
        print(f"->Produto:{product} Quantidade em estoque: {products[product].get('amount')} unidades - Preço: R$ {products[product].get('price')} \n")


def sell_produts(products, sales_record):
    print("----VENDER PRODUTO----\n")
    name = input("Informe o nome do produto vendido: ")
    if name in products:
        amount = int(input(f"Informe a quantidade de {name} vendidos: "))

        if amount > products[name].get('amount'):
            print("NOSSO ESTOQUE É INFERIOR A QUANTIDADE QUE DESEJA VENDEER!")
        
        else:
            products[name]
        
            

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
            

main()
