while(1):
  idade=(int(input("\nDigite sua idade aqui: ")))

  if(5<=idade<=7):
    print("\nCategoria infantil A\n")
  
  if(8<=idade<=11):
    print("\nCategoria infantil B\n")

  if(12<=idade<=13):
    print("\nCategoria Juvenil A\n")

  if(14<=idade<=17):
    print("\nCategoria Juvenil B\n")

  if(idade>=18):
    print("\nCategoria Adulto\n")

  escolha=(input("\nDeseja continuar? s/n \n"))

  if(escolha=="n"):
    break 