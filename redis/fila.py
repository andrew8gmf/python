import redis
r = redis.Redis(host='localhost', port=6379, db=0)

def Adicionar():
    nome = str(input("\nNome: "))
    email = str(input("Email: "))
    telefone = str(input("Telefone: "))
    r.rpush('fila', email)

def Exibir():
    print("\nFila: ")
    print(r.lrange('fila', 0, -1))

def Remover():
    index = r.lindex('fila', 0)
    print("\nRemovido: ")
    print(index)
    r.ltrim('fila', 1, -1)
    
while(True):
    print("\nTRABALHO PRÁTICO - REDIS\n(1) Adicinar uma pessoa na fila\n(2) Exibir fila\n(3) Remover o primeiro da fila")
    op = int(input("Opção: "))

    if(op == 1):
        Adicionar()
    elif(op == 2):
        Exibir()
    elif(op == 3):
        Remover()