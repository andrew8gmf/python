import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def UltimoFila():
    if(r.lrange("fila", 0, 0)==[]):
        return 1000
    else:
        t = r.lrange("fila", -1, -1)
        return int(t[0]) + 1

def Adicionar():
    nome = str(input("\nnome:"))
    email = str(input("e-mail:"))
    telefone = str(input("telefone:"))
    key = UltimoFila()
    r.hset(key, "id", key)
    r.hset(key, "nome", nome)
    r.hset(key, "email", email)
    r.hset(key, "telefone", telefone)
    r.rpush("fila", key)

def Exibir():
    user = r.lrange("fila", 0, -1)
    for u in user:
        print(r.hgetall(u))

def Remover():
    if(r.lrange("fila", 0, 0)==[]):
        print("Fila Vazia")
    else:
        key = r.lpop("fila")
        print(r.hgetall(key))
        r.delete(key)
    
while(True):
    
    print("\nTRABALHO PRÁTICO - REDIS\n(1) Adicinar uma pessoa na fila\n(2) Exibir fila\n(3) Remover uma pessoa na fila")
    op = int(input("Opção:"))

    if(op == 1):
        Adicionar()
    elif(op == 2):
        Exibir()
    elif(op == 3):
        Remover()