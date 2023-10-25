def date():
    while True:
        try:
            date_number = int(input("Informe um mês pelo seu valor númerico: "))
            if date_number > 12 or date_number <= 0:
                raise NameError("Erro")
            return date_number 
        except ValueError:
            print("[ERRO] o número digitado não é um inteiro!")
        except NameError:
            print("O número digitado não corresponde a nenhum mês!")
    
def date_number_for_mounth(date_months, date_number):
    try:
        for mounth in range(len(date_months)):
            if date_months[mounth][1] == date_number:
                mounth = date_months[mounth][0]
                return mounth

    except BaseException as error:
        print("[ERRO]Ocorreu um erro!", error)
                
                
def main():
    date_months = [("Janeiro", 1), ("Fevereiro", 2), ("Março", 3), ("Abril", 4), ("Maio", 5), ("Junho", 6),
                ("Julho", 7), ("Agosto", 8), ("Setembro", 9), ("Outubro", 10), ("Novembro", 11), ("Dezembro", 12)]
    date_number = date()
    mounth = date_number_for_mounth(date_months, date_number)
    print(mounth)

main()
