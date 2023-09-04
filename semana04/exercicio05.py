def ler_vogais(text, vogais):
    for letra in text:
        if letra not in vogais and letra == "a" or letra =="e" or letra == "i" or letra =="o" or letra == "u":
            vogais[letra] = 1
        elif letra in vogais:
            vogais[letra] += 1
    return vogais

def main():
    text = str(input("Informe um texto: ")).lower()
    vogais = {}
    ler_vogais(text, vogais)
    print(vogais)
    
main()
