while True:
  valor, valor_contrato = map(str, input().split())

  if valor == "0" and valor_contrato == "0":
    break

  auxiliar = 0
  valor_contrato = list(valor_contrato)
  lista = []
  lista_final = []

  #Retirar os valores iguais
  for i in range(len(valor_contrato)):
    if valor != valor_contrato[i]:
      lista.append(int(valor_contrato[i])) 

  for i in lista:
    if auxiliar == 0:
      if i != 0:
        lista_final.append(i)
        auxiliar+= 1
    else:
      lista_final.append(i)
      auxiliar+= 1

  if(sum(lista)==0):
    print("0")
  else:
    for i in lista_final:
      print(i,end=" ".strip())
    print("")