###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Conjectura de Collatz
# Nome: Guilherme Henrique Ichiro Seto Ito
# RA: 238706
###################################################

# Inicialização das variáveis

N = int(input())
for i in range (N):
    X = int(input())
    a = X
    ODD = 1
    EVEN = 0
    MAX = 0
    if a > MAX:
        MAX = a
    while a > 1:
        if a % 2 ==0:
            a = a // 2
            EVEN = EVEN + 1
        else:
            a = 3 * a + 1
            ODD+=1
        if a > MAX:
            MAX = a
    print("Valor inicial:", X)
    print("Numeros Pares:", EVEN)
    print("Numeros Impares:", ODD)
    print("Maior Numero:", MAX)

