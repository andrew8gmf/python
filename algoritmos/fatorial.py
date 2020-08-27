n = int(input('Digite um número: '))
if(n<0):
    print('não pode ser 0')
else:
    fat=1
    for i in range(n, 0, -1):
        fat *= i
    print("Fatorial: ", fat)
