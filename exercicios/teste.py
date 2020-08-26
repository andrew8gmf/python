n = int(input('Digite o total de vértices: '))

a = [0]*n
for i in range(n):
    a[i] = [0]*n

    for j in range(n):
        a[i][j] = 0

for j in a:
    print(j)