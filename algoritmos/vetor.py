n=int(input('Digite uma quantia: '))
a=0
lista=[]

while(a<=n):
    print(a)
    a=a+1
    lista.append(a)

    if (a==n):
        print(a)
        print("minimo: ",min(lista))
        print("maximo: ",max(lista))
        break