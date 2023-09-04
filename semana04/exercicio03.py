filmes = {}

for i in range(6):
    name = str(input("Informe o nome do filme: "))
    detals = {}
    detals["vilao"] = str(input("Informe o vilão do filme: "))
    detals["ano"] = int(input("Informe o ano deste filme: "))
    filmes[name] = detals
    
for f in filmes:
    print(f"Nome do filme {f}, vilão {filmes[f].get('vilao')} e o ano deste filme {filmes[f].get('ano')} ")
    
    
