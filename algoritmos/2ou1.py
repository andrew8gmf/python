while(1):
    a = int(input('Jogador A: '))
    if(a < 1 or a > 2):
        print('2 ou 1')
        break

    b = int(input('Jogador B: '))
    if(b < 1 or b > 2):
        print('2 ou 1')
        break

    c = int(input('Jogador C: '))
    if(c < 1 or c > 2):
        print('2 ou 1')
        break

    if (a==b and a==c):
        print("Empate")
        break
    else:
        if (a==b):
            print("C ganhou")
            break
        else:
            if (b==c):
                print("A ganhou")
                break
            else:
                print("B ganhou")
                break