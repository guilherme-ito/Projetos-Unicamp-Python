###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Batalha na Ponte de Piltover
# Nome: Guilherme Henrique Ichiro Seto Ito
# RA: 238706
###################################################

hp_jinx = int(input())
hp_ekko = int(input())

# Leitura dos ataques da Jinx
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
    if hp_ekko > hp_jinx:
        list[i] = list[i] // 2
    hp_ekko = hp_ekko - list[i]
    if hp_ekko <= 0:
        hp_ekko = 0

# Leitura dos ataques do Ekko
if hp_ekko > 0:
    m = int(input())
    list = []
    for j in range(m):
        list.append(int(input()))
        if hp_ekko < hp_jinx:
            list[j] = list[j] // 2
        hp_jinx = hp_jinx - list[j]
        if hp_jinx <= 0:
            hp_jinx = 0

    # Impressão das informações de saída
    print('Vida da Jinx:', hp_jinx)
    print('Vida do Ekko:', hp_ekko)
    if hp_jinx > hp_ekko:
        print('Jinx foi a vencedora da batalha')
    elif hp_ekko > hp_jinx:
        print('Ekko foi o vencedor da batalha')
    elif hp_ekko == hp_jinx:
        print('A batalha terminou empatada')

elif hp_ekko <= 0:
    print('Vida da Jinx:', hp_jinx)
    print('Vida do Ekko:', hp_ekko)
    if hp_jinx > hp_ekko:
        print('Jinx foi a vencedora da batalha')
    elif hp_ekko > hp_jinx:
        print('Ekko foi o vencedor da batalha')
    elif hp_ekko == hp_jinx:
        print('A batalha terminou empatada')
    

