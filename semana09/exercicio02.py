def avaliar_produto():
    while True:
        try:
            avaliacao = int(input("Informe uma avaliação ao nosso produto de 0 a 10: "))
            assert 0 < avaliacao < 10, "Avaliação fora do intervalo permitido (0 a 10)"

        except ValueError:
            print("Você informouum valor inválido")

        except AssertionError as e:
            print(f"[ERRO] {e}")

        else:
            return avaliacao

def main():
    avaliacao = avaliar_produto()
    print(f"A avalição do produto foi {avaliacao}")

main()
