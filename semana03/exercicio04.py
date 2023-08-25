largest_value = [0, 0]
matriz = [
    [1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]

diagonal = 1
for line in range(len(matriz)):
    horizontal = 1
    vertical = 1
    for column in range(len(matriz[line])):
        horizontal *= matriz[line][column]
        if horizontal > largest_value[0]:
            largest_value[0] = horizontal
            largest_value[1] = f"horizontal: {line}"

        vertical *= matriz[column][line]
        if vertical > largest_value[0]:
            largest_value[0] = vertical
            largest_value[1] = f"vertical: {line}"

        if column == line:
            diagonal *= matriz[line][column]
            if diagonal > largest_value[0]:
                largest_value[0] = diagonal
                largest_value[1] = "Diagonal principal"

print("O maior valor é da", largest_value[1], "que resultou em", largest_value[0])

