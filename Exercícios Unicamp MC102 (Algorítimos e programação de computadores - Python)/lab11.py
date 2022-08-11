#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Batalha Naval
# Nome:
# RA:
#####################################################

# Leitura da matriz
ln = {} #localização dos navios
matriz = []
for _ in range(10):
    matriz.append(input().split())
#Dicionário das localizações
for a in range(10):
    for b in range(10):
        Q = matriz[a][b]
        if not Q == '.':
            if not Q in ln:
                ln[Q] = 1
            else:
                ln[Q] += 1
p = int(input()) #quantas jogadas tem
for i in range(p):
    lc = input() #leitura de linhas e colunas
    atk = lc.split()
    k =atk[0]
    l =int(atk[1])-1
    if k == "A":
        k = 0
    if k == "B":
        k = 1
    if k == "C":
        k = 2
    if k == "D":
        k = 3
    if k == "E":
        k = 4
    if k == "F":
        k = 5
    if k == "G":
        k = 6
    if k == "H":
        k = 7
    if k == "I":
        k = 8
    if k == "J":
        k = 9
    if matriz[k][l] == ".":
        print("agua")
    elif matriz[k][l] != ".":
        x = matriz[k][l]
        ln[x] -= 1
        if ln[x] >= 1:
            print("atingiu o navio",x)
        elif ln[x] == 0:
            print("afundou o navio",x)
















# Dica: Você pode usar um dicionario para gravar quantas
# partes de um navio ainda devem ser atingidas para afundá-lo
