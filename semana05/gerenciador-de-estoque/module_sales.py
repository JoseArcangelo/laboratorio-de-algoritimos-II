import datetime

def sell_produts(stock, sales_record, historical_changes):
    """Função que realiza a venda de um produto, atualizando o estoque, calculando o valor da venda,
    e registrando o valor da vendas no histórico de vendas com a data da mesma,
    ela recebe como parâmetros o estoque, histórico de vendas e o historico de alterações."""
    
    print("\n----VENDER PRODUTO----")
    name_product = input("Informe o nome do produto vendido: ")
    if name_product in stock:
        quantity_sell = int(input(f"Informe a quantidade de {name_product} vendidos: "))
        if quantity_sell > stock[name_product]["amount"]:
            print("OPS! O ESTOQUE NÃO POSSUO A QUANTIDADE QUE DESEJA VENDER!")
        else:
            stock[name_product]["amount"] -= quantity_sell
            profit_sale = quantity_sell * stock[name_product]['price_historic'][-1]
            print("Valor total da venda: R$", profit_sale)
            date_now = datetime.datetime.now()
            date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min"
            sales_record.append(f"Nome do produto: {name_product} - Quantidade vendida: {quantity_sell} - Lucro da venda: R$ {profit_sale} - Data: {date_now}")

            if stock[name_product]["amount"] == 0:
                stock.pop(name_product)
                historical_changes.append(f"O produto {name_product} foi removido do estoque pois esgotou - DATA {date_now}")

    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")
    return stock, sales_record, historical_changes

