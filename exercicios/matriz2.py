#b) Gerar uma matriz identidade
matriz = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]

diag = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            diag.append(matriz[i][j])

print(diag)