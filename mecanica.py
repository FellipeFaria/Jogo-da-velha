import lista 


jogador_jogadas, cpu_jogadas = [], []

def mostra_tabela(tabela):
  for i in tabela:
    for j in i:
      print(' ', j, end='')
    print(' ')


def coloca_jogada(tabela, jogada, simbolo):
  sim = ' '
  if simbolo == 'X':
    sim = 'X'
    jogador_jogadas.append(jogada)
  elif simbolo == 'O':
    sim = 'O'
    cpu_jogadas.append(jogada)

  if jogada == 1:
    tabela[0][0] = sim
  if jogada == 2:
    tabela[0][2] = sim
  if jogada == 3:
    tabela[0][4] = sim
  if jogada == 4:
    tabela[2][0] = sim
  if jogada == 5:
    tabela[2][2] = sim
  if jogada == 6:
    tabela[2][4] = sim
  if jogada == 7:
    tabela[4][0] = sim
  if jogada == 8:
    tabela[4][2] = sim
  if jogada == 9:
    tabela[4][4] = sim


def checa_ganhador():
  vitoria_opc = (
    (1,2,3), (4,5,6), (7,8,9),
    (1,4,7), (2,5,8), (3,6,9),
    (1,5,9), (3,5,7)
  )

  for i in vitoria_opc:
    if lista.tuplaEmLista(i, jogador_jogadas):
      return 'Jogador GANHOU!!!'
    elif lista.tuplaEmLista(i, cpu_jogadas):
      return 'CPU GANHOU!!!'
    elif len(jogador_jogadas) + len(cpu_jogadas) == 9:
      return 'DEU VELHA!!!'
        
  return ''
