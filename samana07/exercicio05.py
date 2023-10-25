def menu():
    print("\n1 - DEPOSITAR")
    print("2 - SACAR")
    print("3 - VERIFICAR SALDO BANCÁRIO")
    print("4 - HISTÓRICO DE MOVIMENTAÇÕES")
    print("5 - SAIR")
    option = input("Informe a opção desejada: ")
    return option

def deposit(bank_account):
    try:
        value_deposit = float(input("Infome o valor que deseja depositar: "))
        if value_deposit > 0:
            bank_account['balance'] += value_deposit
            bank_account['historic'].append(f"Depostitados R$  {value_deposit}")
            print(f"O DEPÓSITO DE R$ {value_deposit} FOI REALIZADO COM SUCESSO!")
            return bank_account
            
        else:
            print("O valor que você informou é inválido, pois ele não pode ser menor ou igual a 0!")
    
    except ValueError:
        print("VALOR INVÁLIDO!!")

def withdraw(bank_account):
    try:
        value_withdraw = float(input("Informe o valor que você deseja sacar: "))
        if value_withdraw > bank_account['balance']:
            print("SEU SALDO É INSUFICIENTE!")
            
        elif value_withdraw > bank_account['transaction_limit']:
            print("SEU LIMITE É INFEIROR AO VALOR INFORMADO!")
            
        elif value_withdraw <= 0:
            print("O valor que você informou é inválido, pois ele não pode ser menor ou igual a 0!")
            
        else:
            bank_account['balance'] -= value_withdraw
            bank_account['historic'].append(f"Sacados R$ {value_withdraw}")
            print(f"O SAQUE DE R$ {value_withdraw} FOI REALIZADO COM SUCESSO!")
            return bank_account
    except ValueError:
        print("VALOR INVÁLIDO!!")

def see_balance(bank_account):
    print("\nSALDO BNCÁRIO:")
    print(f"Seu saldo é R$ {bank_account['balance']}")
    
def historic_movimentation(bank_account):
    if len(bank_account['historic']) == 0:
        print("NENHUMA MOVIMENTAÇÃO FOI REALIZADA!")
    else:
        print("HISTORICO DE MOVIMENTAÇÕES:")
        for i in bank_account['historic']:
            print(i)

def main():
    bank_account = {
        "balance": 3000, "transaction_limit": 1000, "historic": []}
    
    while True:
        option = menu()
        
        if option == "1":
            bank_account = deposit(bank_account)

        elif option == "2":
            withdraw(bank_account)
            
        elif option == "3":
            see_balance(bank_account)
            
        elif option == "4":
            historic_movimentation(bank_account)

        elif option == "5":
            print("Saindo...")
            break
        
        else:
            print("OPÇÃO INVÁLIDA!!!")
    
main()
