def adicionar_alunos(dicionario_alunos):
    while True:
        name = str(input("Informe o nome do aluno: "))
        if name == "":
            return dicionario_alunos
        notas = {}
        notas["n1"] = float(input("Informe a primeira nota do aluno: "))
        notas["n2"] = float(input("Informe a segunda nota do aluno: "))
        dicionario_alunos[name] = notas

def media(dicionario_alunos):
    for aluno in dicionario_alunos:
        media = 0
        media = (dicionario_alunos[aluno].get("n1") + dicionario_alunos[aluno].get("n2")) / len(dicionario_alunos[aluno])
        print(f"A media do aluno {aluno} é {media}")
        
def main():
    dicionario_alunos = {}
    adicionar_alunos(dicionario_alunos)
    media(dicionario_alunos)
    
main()
