import random

def create_file(amount):
    file = open('number.txt', 'w')

    for i in range(amount):
        file.write(str(random.randint(0, 100)))
        file.write(",")

    file.close()
        
def calculate_average():
    file = open('exercicio01/number.txt', 'r')
    line_lines = file.readlines()
    file.close()
    line_lines = line_lines[0]
    line_lines = line_lines.split(",")
    average = 0

    for number in line_lines:
        average += int(number)
    average = average / len(line_lines)
    return average
   
def main():
    create_file(5)
    average = calculate_average()
    print("A media destes numeros no arquivo é ", average)

main()
