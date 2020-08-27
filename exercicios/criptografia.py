while 1:

  e=input("\n1-Encriptar \n2-Decriptar \n3-Sair\n\n")

  if (e=="1"):
    texto = input("\nDigite um texto: ")
    #print(texto)
    for x in texto:
      #print(x)
      codificado=ord(x)
      #print(codificado)
      codificado=(codificado+5)
      decodificado=chr(codificado)
      print(decodificado)

  if (e=="2"):
    texto = input("\nDigite um texto: ")
    #print(texto)
    for x in texto:
      #print(x)
      codificado=ord(x)
      #print(codificado)
      codificado=(codificado-5)
      decodificado=chr(codificado)
      print(decodificado) 
 
  if (e=="3"):
    break