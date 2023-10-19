def ler_year():
    while True:
        try:
            ano = int(input("Informe o ano para verificar se é bissexto: "))
            if ano < 0:
                raise NameError("zero_error")
            return ano

        except ValueError:
            print("[ERRO] VOCÊ INFORMOU UM VALOR INVÁLIDO!")
        except NameError:
            print("[ERRO] VOCÊ INFORMOI UM VALOR MENOR QUE 0!")

def verificar_bissexto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        resposta = ("O ano é bissexto!")
    else:
        resposta = ("O ano não é bissexto!")
    return resposta

def main():
    while True:
        year = ler_year()
        resposta = verificar_bissexto(year)
        print(resposta)
main()
