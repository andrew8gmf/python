import random

print("\nEscolha o tipo da matriz que será gerada: ")
escolha=int(input("\n1-Matriz diagonal \n2-Matriz identidade \n3-Matriz simétrica\n\n"))

escolha2=int(input("\nDigite a ordem desejada: "))

ordem=escolha2-1

#a) Gerar uma matriz diagonal
if (escolha==1):
    matriz = [[1, 2, 3],
            [7, 8, 9],
            [4, 5, 2]]

    print(matriz)

    diag = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                diag.append(matriz[i][j])

    print(diag)

#b) Gerar uma matriz identidade
if (escolha==2):
    matriz = [[1, 0, 0], 
            [0, 1, 0],
            [0, 0, 1]]

    diag = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                diag.append(matriz[i][j])

    print(diag)

#c) Gerar uma matriz simétrica
if (escolha==3):
    matriz = [[1, 2, 3],
            [2, 6, 4],
            [3, 4, 5]]

    print(matriz)