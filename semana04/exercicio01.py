biblioteca = {}

for pessoa in range(5):
    name = str(input("Informe o nome da pessoa: "))
    biblioteca[name] = str(input("Informe a cor da camisa dessa pessoa: "))
print(biblioteca)
