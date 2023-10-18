def input_int(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError as error:
            print("ERRO")

        except BaseException as error:
            print("[ERRO] Ocorreu um erro!", error)

def division_numbers(number_one, number_two):
    while True:
        try:
            result = number_one / number_two
            return result
        except BaseException as error:
            print("[ERRO] Ocorreu um erro na divisao!", error)

def main():
    number_one = input_int("Informe o primeiro número: ")
    number_two = input_int("Informe o segundo número: ")
    result = division_numbers(number_one, number_two)
    print(result)
    
main()
