#ler os dados inteiros
quantidade_leitura = int(input())
contador = 0
pares = []
impares = []

while(contador < quantidade_leitura):
  numero = int(input())
  if(numero % 2 == 0):
    pares.append(numero)
  else:
    impares.append(numero)
  
  contador += 1

pares.sort()
impares.sort(reverse=True)

for par in pares:
  print(par)

for impar in impares:
  print(impar)