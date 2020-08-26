valortotal=0.0

while(1):
  cod=(int(input("\nInsira o código do produto: ")))

  if(100<=cod<=106):
    qnt=(float(input("Digite a quantidade: ")))

    if (cod == 100):
      print("Produto: Cachorro quente")
      valorparcial=1.20*qnt
      
    if (cod == 101):
      print("Produto: Bauru simples")
      valorparcial=1.30*qnt
      
    if (cod == 102):
      print("Produto: Bauru com ovo")
      valorparcial=1.50*qnt
      
    if (cod == 103):
      print("Produto: Hamburguer")
      valorparcial=1.20*qnt

    if (cod == 104):
      print("Produto: Cheeseburguer")
      valorparcial=1.70*qnt

    if (cod == 105):
      print("Produto: Suco")
      valorparcial=2.20*qnt

    if (cod == 106):
      print("Produto: Refrigerante")
      valorparcial=1.00*qnt

    valortotal=valortotal+valorparcial
    escolha=(input("\nDeseja a conta? s/n \n"))

    if(escolha=="s"):
      break

print("\nValor a ser pago: R$",valortotal)