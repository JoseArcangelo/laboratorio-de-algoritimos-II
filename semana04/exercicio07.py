def menu():
    print("1 - Adicionar contato")
    print("2 - Incluir telefone")
    print("3 - Deletar telefone")
    print("4 - Deletar contato")
    print("5 - Pesquisar contato")
    print("6 - Sair da agenda")
    opc = int(input("Informe a opção desejada: "))
    return opc

def create_contact(agenda):
    name = str(input("Informe o nome da pessoa que deseja incluir na agenda: "))
    agenda[name] = []
    total_numbers = int(input("Quantos telefones deseja incluir ao contato: "))
    for telefones in range(total_numbers):
        number = int(input("Informe o telefone que deseja incluir: "))
        agenda[name].append(number)
    print("CONTATO REGISTRADO NA AGENDA!")
    
    return agenda
    
def include_phone(agenda):
    contact = str(input("Informe o nome do contato que deseja incluir um telefone: "))
    
    if contact in agenda:
        number = int(input("Informe o telefone que deseja adionar:"))
        agenda[contact].append(number)
        print("NÚMERO DE TELEFONE SALVO NO CONTATO!")
    else:
        print("Este contato não existe em sua agenda")
        incluir = str(input("Deseja inclui-lo em sua agenda?(Sim/Não)")).upper()
        if incluir == "SIM":
            create_contact(agenda)
        return agenda
        
def delete_phone(agenda):
    name = str(input("Informe o nome do contato que deseja remover um telefone: "))
    if name not in agenda:
        print("ESTE CONTATO NÃO CONSTA EM SUA AGENDA!")
        
    else:
        number = int(input("Informe o númeo de telefone que deseja deletar deste contato: "))
        if number in agenda[name]:
            agenda[name].remove(number)
            print("NÚMERO DE TELEFONE REMOVIDO DO CONTATO!")
        else:
            print("ESTE NÚMERO DE TELEFONE NÃO EXISTE NESTE CONTATO!")
     
    return agenda
        
def delete_contact(agenda):
    name = str(input("Informe o nome do contato que deseja remover de sua agenda: "))
    if name in agenda:
        agenda.pop(name)
        print("CONTATO REMOVIDO!")
    
    else:
        print("ESTE CONTATO NÃO EXISTE EM SUA AGENDA!")
        
    return agenda
    
def get_phones(agenda):
    name = str(input("Informe o nome do contato que deseja pesquisar: "))
    if name in agenda:
        print(f"Telefones salvos de {name}:")
        for number in agenda[name]:
            print(number)
    else:
        print("ESTE CONTATO NÃO EXISTE EM SUA AGENDA!")
    
    return
   
def main():
    opc = 0
    agenda = {}

    while opc != 6:
        opc = menu()
        if opc == 1:
            create_contact(agenda)

        elif opc == 2:
            include_phone(agenda)
            
        elif opc == 3:
            delete_phone(agenda)
            print(agenda)
            
        elif opc == 4:
            delete_contact(agenda)
            
        elif opc == 5:
            get_phones(agenda)
        
        elif opc == 6:
            print("Saindo...")
            
        else:
            print("OPÇÃO INVÁLIDA!")

main()
    
