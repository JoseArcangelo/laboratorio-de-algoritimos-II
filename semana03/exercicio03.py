def dinheiro_entregar(saque):
    cedulas = []
    while saque != 0:
        if saque >= 100:
            cedulas.append(100)
            saque -= 100
        elif saque >= 50:
            cedulas.append(50)
            saque -= 50
        elif saque >= 20:
            cedulas.append(20)
            saque -= 20
        elif saque >= 10:
            cedulas.append(10)
            saque -= 10
            
    print("Cedulas a serem recebidas:")
    if cedulas.count(100) > 0:
        print(cedulas.count(100),"de R$", 100)
    if cedulas.count(50) > 0:
        print(cedulas.count(50),"de R$", 50)
    if cedulas.count(20) > 0:
        print(cedulas.count(20),"de R$", 20)
    if cedulas.count(10) > 0:
        print(cedulas.count(10),"de R$", 10)
    
def main():
    saque = int(input("Informe o valor do saque:"))
    if saque % 10 == 0:
        dinheiro_entregar(saque)
    else:
        print("Valor inválido!")
main()
