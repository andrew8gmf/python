p = []*50
top = 0
end = 0

while True:
  v = input("Digite o vértice a inserir ou Fim para encerrar: ")
  if v == "Fim":
    break
  p.insert(top, v)
  top += 1

v = []*50

while True:
  c = p[top-1]
  if top == 0:
    break
  v.insert(end, c)
  top -= 1
  end += 1

if p == v:
  print("É palindromo")
else:
  print("Não é palindromo")