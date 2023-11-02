import random

def criar_arquivo(amount):
    file = open('number.txt', 'w')

    for i in range(amount):
        file.write(str(random.randint(0, 100)))
        file.write(",")

    file.close()
        
def ler_numbers():
    file = open('number.txt', 'r')
    line_lines = file.readlines()
    line_lines = line_lines[0]
    print(line_lines)
   
    
    file.close()





def main():
    criar_arquivo(20)
    ler_numbers()

main()
