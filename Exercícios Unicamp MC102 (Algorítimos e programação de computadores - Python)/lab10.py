#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Aventura na Amazônia
# Nome:
# RA:
#####################################################

matriz = [['.' for _ in range(20)] for _ in range(20)]    # criando a matriz


inicio = [int(i) for i in input().split()]  # posição inicial
i = inicio[0]
j = inicio[1]
matriz[i][j] = "+"
       # dados das coordenadas
for a in range(400):
    N = input()
    coordenadas =N.split()
    if coordenadas[0] == "A":
        matriz[i][j] = "#"
    elif coordenadas[0] == "S":
        b = int(coordenadas[1])
        for k in range(b):
            if not matriz[i+k+1][j] == "#":
                matriz[i+k+1][j] = "+"
        i = i + b
    elif coordenadas[0] == "N":
        b = int(coordenadas[1])
        for k in range(b):
            if not matriz[i-k-1][j] == "#":
                matriz[i-k-1][j] = "+"
        i = i - b
    elif coordenadas[0] == "L":
        b = int(coordenadas[1])
        for k in range(b):
            if not matriz[i][j+k+1] == "#":
                matriz[i][j+k+1] = "+"
        j = j+b
    elif coordenadas[0] == "O":
        b = int(coordenadas[1])
        for k in range(b):
            if not matriz[i][j-k-1] == "#":
                matriz[i][j-k-1] = "+"
        j = j - b
    elif coordenadas[0] == "F":
        break

# Impressão da matriz

for l in matriz:
    print(" ".join(l))

