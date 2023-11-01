def ler_lados():
    while True:
        try:
            lado1 = float(input("Informe o tamanho do primeiro lado: "))
            lado2 = float(input("Informe o tamanho do segundo lado: "))
            lado3 = float(input("Informe o tamanho do terceiro lado: "))
            if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                raise NameError("[ERRO]")
            return [lado1, lado2, lado3]

        except ValueError:
            print("Você informou um valor inválido!")

        except NameError:
            print("Você informu um valor menor ou igua a 0, ou seja, inválido!")

        except BaseException as e:
            print(f"[ERRO] {e}")

def verificar_triangulo(lados):
    n = len(lados)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lados[j] > lados[j + 1]:
                lados[j], lados[j + 1] = lados[j + 1], lados[j]
    try:
        verificacao = lados[0] + lados[1]
        if verificacao < lados[2]:
            raise ValueError("[ERRO]")

    except ValueError:
        resposta = "TRIÂNGULO INVÁLIDO"
        return resposta

    else:
        if lados[0] == lados[1] and lados[1] == lados[2]:
            resposta = "TRIÂNGULO EQUILÁTERO"

        elif lados[0] == lados[1] or lados[1] == lados[2] or lados[2] == lados[0]:
            resposta = "TIÂNGULO ISÓSCELES"

        else:
            resposta = "TRIÂNGULO ESCALENO"

        return resposta

def main():
    lados = ler_lados()
    resposta = verificar_triangulo(lados)
    print(resposta)


main()
