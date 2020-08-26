#a) Gerar uma matriz diagonal
matriz = [[1, 2, 3, 4, 5],
           [7, 8, 9, 3, 8],
           [4, 5, 2, 3, 4],
           [2, 3, 4, 5, 3],
           [4, 5, 3, 4, 5]]

diag = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            diag.append(matriz[i][j])

print(diag)