import datetime

def sell_produts(stock, sales_record):
    print("\n----VENDER PRODUTO----")
    name = input("Informe o nome do produto vendido: ")
    if name in stock:
        quantity_sell = int(input(f"Informe a quantidade de {name} vendidos: "))
        if quantity_sell > stock[name]["amount"]:
            print("NOSSO ESTOQUE É INFERIOR A QUANTIDADE QUE DESEJA VENDER!")
        else:
            stock[name]["amount"] -= quantity_sell
            profit_sale = quantity_sell * stock[name]["price_historic"][-1]
            print("Valor total da venda: R$", profit_sale)
            date_now = datetime.datetime.now()
            date_now = f"{date_now.year}/{date_now.month}/{date_now.day} {date_now.hour} horas {date_now.minute} min"
            sales_record.append(f"Nome do produto: {name} - Quantidade vendida: {quantity_sell} - Lucro da venda: R$ {profit_sale} - Data: {date_now}")

            if stock[name]["amount"] == 0:
                stock.pop(name)
    else:
        print("OPS! NÃO POSSUIMOS ESTE PRODUTO!")
    return stock, sales_record


