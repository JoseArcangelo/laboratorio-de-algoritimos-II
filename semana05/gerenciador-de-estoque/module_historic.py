def sales(sales_record):
    """Função que lista todas as vendas realizadas,
    ela recebe como parametros o historico de vendas."""

    print("\n--RELATÓRIO DE VENDAS--")
    if len(sales_record) == 0:
        print("OPS! Nenhuma venda foi realizada")
    else: 
        for sale in sales_record:
            print(sale)

def see_historical_change(historical_changes):
    """Função que lista todas as alterações no estoque, incluindoatualizações, adições 
    e exclusões, ela recebe como parametros o historico de alterações."""

    print("--\nHistórico de alterações--")
    if len(historical_changes) == 0:
        print("OPS! Nenhuma venda foi realizada")
    else:
        for historic in historical_changes:
            print(historic)

