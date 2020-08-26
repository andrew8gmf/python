salario=float(input("\nDigite seu salário: "))
prestacao=int(input("\nDigite o valor da prestação do empréstimo: "))

vps=salario*0.20

if(prestacao >= vps):
  print("\nEmpréstimo não concedido")
else:
  print("\nEmpréstimo concedido")
