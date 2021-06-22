acumulador = 0
valores = []
quantidade_teste = int(input())
for item in range(quantidade_teste):
  valor_leds = input()
  valores.append(valor_leds)      

for valor in valores:
  for letra in valor:
    if letra == "0":
      acumulador+= 6
    elif letra == "1":
      acumulador+= 2
    elif letra == "2":
      acumulador+= 5
    elif letra == "3":
      acumulador+= 5
    elif letra == "4":
      acumulador+= 4
    elif letra == "5":
      acumulador+= 5
    elif letra == "6":
      acumulador+= 6    
    elif letra == "7":
      acumulador+= 3
    elif letra == "8":
      acumulador+= 7
    elif letra == "9":
      acumulador+= 6
  print("{} leds".format(acumulador))
  acumulador = 0