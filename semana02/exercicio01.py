def inverter_lista(l1, l2):
    contador = len(l1)
    for i in range(len(l1)):
        contador = contador - 1
        l2.append(l1[contador])
    return l2
    
def main():
    l1 = [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l1)
    l2 = []
    l2 = inverter_lista(l1, l2)
    print(l2)
    
main()
