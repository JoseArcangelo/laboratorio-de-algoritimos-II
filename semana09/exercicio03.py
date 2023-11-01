def ler_number_raiz():
  while True:
    try:
      number = float(input("Informe o número: "))
      if number < 0:
        raise NameError("NegativeNumberError ")
      raiz = number ** (1/2)
      return raiz, number
    
    except ValueError:
      print("Valor inválido!")

    except NameError as e:
      print(e)

def main():
  raiz, number = ler_number_raiz() 
  print(f"A raiz quadrada de {number} é {raiz}")

main()
