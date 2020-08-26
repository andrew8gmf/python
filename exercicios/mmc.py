def line_():
  print(' ')
  print('-'*30)
  print(' ')

num1=int(input("\nDigite um número: "))
num2=int(input("Digite outro número: "))

if( num1>num2):
  maior=num1
else:
  maior=num2

while(True):
  if maior%num1==0 and maior%num2==0:
    line_()
    print(maior)
    break
  else:
    maior+=1
