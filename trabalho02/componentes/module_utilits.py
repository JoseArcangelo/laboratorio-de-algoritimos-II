import os

def clear_terminal():
    """Função que limpa o terminal"""
    if os.name == 'posix': 
        return os.system('clear')  
    elif os.name == 'nt': 
        return os.system('cls') 
