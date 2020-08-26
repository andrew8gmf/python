nome = input("\nDigite seu nome: ")
materia = input("Nome da matéria: ")

nota1 = float(input("\nDigite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

media = (nota1+nota2+nota3+nota4)/4
print("\nMédia: ", media)

if media < 6:
  print("\nREPROVADO!")

if 6 <= media < 8:
  print("\nMÉDIA BOA!")

if 8 <= media:
  print("\nPASSOU COM LOUVOR!")
