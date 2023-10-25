import math
def n_grupo1(total_alunos):
    while True:
    
        try:
            grupo1 = int(input("Informe o total de integrantes do grupo 1: "))
            if grupo1 >= total_alunos:
                 raise NameError("Erro")
            elif grupo1 <= 0:
                print("O total de integrantes do grupo não pode ser menor ou igual a 0!")
            else:
                return grupo1
        except ValueError:
            print("Valor inválido!")
            
        except NameError:
            print("O total de integrantes do grupo 1 não pode ser maior ou igual ao total de alunos!")
        
def main():
    while True:
        try:
            total_alunos = int(input("Informe o numero total de alunos: "))
            if total_alunos <= 0:
                print("Informe um valor maior que 0")
            else:
                break
            
        except ValueError:
            print("Valor inválido!")
    
    grupo1 = n_grupo1(total_alunos)
    combinacoes_possiveis = math.comb(total_alunos, grupo1) 
    print(combinacoes_possiveis)   
main()
