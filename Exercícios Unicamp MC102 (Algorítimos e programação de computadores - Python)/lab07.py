###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Encaixe Perfeito
# Nome: Guilherme Ito
# RA: 238706
###################################################

# Leitura do número de partidas
n = int(input())

for a in range(n):
  # Leitura das peças 1 e 2
  P1 = [int(i) for i in input().split()]
  P2 = [int(i) for i in input().split()]
  c = len(P2) - len(P1) + 1
  lista_espaçosvazios = []
  for b in range(c):
    somacolunas = []
    for j in range (len(P1)):
      x = P1[j] + P2[j+b]
      somacolunas.append(x) ## somamo as coluna
    maior = max(somacolunas)
    espaços_vazios = []
    for k in range (len(somacolunas)):
      espaços_vazios.append(maior-somacolunas[k]) ##pontuação de cada andada
    P = sum(espaços_vazios) ##pontuação de cada andada em numero
    lista_espaçosvazios.append(P)
    P=0

  P1.reverse()
  for b in range(c):
    somacolunas = []
    for j in range (len(P1)):
      x = P1[j] + P2[j+b]
      somacolunas.append(x) ## somamo as coluna
    maior = max(somacolunas)
    espaços_vazios = []
    for k in range (len(somacolunas)):
      espaços_vazios.append(maior-somacolunas[k]) ##pontuação de cada andada
    P = sum(espaços_vazios) ##pontuação de cada andada em numero
    lista_espaçosvazios.append(P)
    P=0



  minimo = min(lista_espaçosvazios)
  if minimo == 0:
    print("Encaixe Perfeito!")
  else:
    print("Pontuacao:", minimo)
  if lista_espaçosvazios.index(minimo)+1 <=c:
    print("Posicao de Encaixe:",lista_espaçosvazios.index(minimo)+1)
  else:
    print("Posicao de Encaixe:", lista_espaçosvazios.index(minimo) + 1- c)
  if lista_espaçosvazios.index(minimo) <= len(lista_espaçosvazios)/2 -1:
    print("Peca 1: Normal")
  else:
    print("Peca 1: Invertida")








# Processamento das possibilidades de encaixe



  # Impressão da saída esperada para cada partida
  '''print("Pontuacao:", P)
  print("Encaixe Perfeito!")
  print("Posicao de Encaixe:", R)
  print("Peca 1:", S)'''
