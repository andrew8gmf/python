hora=int(input("\nQuanto você ganha por hora: "))
nhora=int(input("Número de horas trabalhadas no mês: "))

salbruto=hora*nhora

if (salbruto<=900):
  descontoir=1

if (salbruto>=900 and salbruto<=1500):
  descontoir=0.05

if (salbruto>=1500 and salbruto<=2500):
  descontoir=0.10

if (salbruto>2500):
  descontoir=0.20

ir=salbruto*descontoir
#sindicato=salbruto*0.03
inss=salbruto*0.10
fgts=salbruto*0.11
descontos=ir+inss

salliq=salbruto-descontos

print("\nSalário bruto:",salbruto)
print("IR:",ir)
print("INSS:",inss)
print("FGTS:",fgts)
print("Total de descontos:",descontos)
print("Salário líquido:",salliq)