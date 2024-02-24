def tuplaEmLista(tupla, lista):
  c = 0

  for i in tupla:
    if i in lista:
      c+=1

  t = c == len(tupla)

  return t
