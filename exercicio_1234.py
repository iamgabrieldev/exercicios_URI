while True:
  try:
    frase = input()
    frase_auxiliar = ""

    PrimeiraLetra = True

    for letra in frase:
      if letra == ' ':
        frase_auxiliar += " "
        continue
      if PrimeiraLetra:
        frase_auxiliar += letra.upper()
        PrimeiraLetra = False
      else:
        frase_auxiliar+= letra.lower()
        PrimeiraLetra = True

    print(frase_auxiliar)
  except EOFError
    break