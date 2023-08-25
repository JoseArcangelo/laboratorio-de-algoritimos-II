import random
cartela = []
l_auxiliar = []

def sorteio_number():
    number = random.randint(0, 99)
    return number

for linha in range(5):
    cartela.append([])
    for colunm in range(5):
        number = sorteio_number()
        while number in l_auxiliar:
            number = sorteio_number()
        l_auxiliar.append(number)
        cartela[linha].append(number)

print(cartela)
