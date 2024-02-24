import random as rand
import mecanica as mec


resultado = ''

tabela = [
  [' ', '|', ' ', '|', ' '],
  ['-', '+', '-', '+', '-'],
  [' ', '|', ' ', '|', ' '],
  ['-', '+', '-', '+', '-'],
  [' ', '|', ' ', '|', ' ']
]

mec.mostra_tabela(tabela)

while resultado == '':
  jogador = int(input('Onde você vai jogar? (1-9): '))

  while jogador in mec.cpu_jogadas or jogador in mec.jogador_jogadas:
    print('Você não pode jogar aqui!')
    jogador = int(input('Onde você vai jogar? (1-9): '))
  
  mec.coloca_jogada(tabela, jogador, 'X')
  resultado = mec.checa_ganhador()

  cpu = rand.randint(1, 9)

  while cpu in mec.jogador_jogadas or cpu in mec.cpu_jogadas:
    cpu = rand.randint(1, 9)
  
  mec.coloca_jogada(tabela, cpu, 'O')
  resultado = mec.checa_ganhador()

  mec.mostra_tabela(tabela)

print('FIM DE JOGO')
print(resultado)
