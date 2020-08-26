hora=int(input("\nQuanto você ganha por hora: "))
nhora=int(input("Número de horas trabalhadas no mês: "))

salbruto=hora*nhora

ir=salbruto*0.11
inss=salbruto*0.08
sindicato=salbruto*0.05
descontos=ir+inss+sindicato

salliq=salbruto-descontos

print("\nSalário bruto:",salbruto)
print("IR:",ir)
print("INSS:",inss)
print("Sindicato:",sindicato)
print("Salário líquido:",salliq)