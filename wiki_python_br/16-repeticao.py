#a, b = 0, 1
a=0
b=1

while b < 500:
  print(b)
  a, b = b, a+b
  #a=b
  #b=a+b

  if b > 500:
    print(b)
    break