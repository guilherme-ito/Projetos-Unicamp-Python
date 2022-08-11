###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Ballon d'Or
# Nome: Guilherme Henrique Ichiro Seto Ito
# RA: 238706
###################################################
L = int(input())
jogadores=[]
dicionario ={}
n = 0
a = 0
b = 0
c = 0
d = 0
for i in range(L*5):
    jogadores.append(str(input()))
for j in range(i+1):
    x = jogadores[j]
    if jogadores.index(x) == 0 or jogadores.index(x) == (5*n): #condição primeiro lugar
        if not x in dicionario:
            dicionario[x] = 6
        else:
            dicionario[x] +=6
        n+=1
    elif jogadores.index(x) == 1 or jogadores.index(x) == 5*a+1:
        if not x in dicionario:
            dicionario[x] = 4
        else:
            dicionario[x] += 4
        a+=1
    elif jogadores.index(x) == 2 or jogadores.index(x) == 5*b+2 : #condição terceiro lugar
        if not x in dicionario:
            dicionario[x] = 3
        else:
            dicionario[x] += 3
        b+=1
    elif jogadores.index(x) == 3 or jogadores.index(x) == 5*c+3: #condição quarto lugar
        if not x in dicionario:
            dicionario[x] = 2
        else:
            dicionario[x] += 2
        c+=1
    elif jogadores.index(x) == 4 or jogadores.index(x) == 5*d+4: #condição quinto lugar
        if not x in dicionario:
            dicionario[x] = 1
        else:
            dicionario[x] += 1
        d+=1
    jogadores[j] = "nada"
for k in sorted(dicionario,key = dicionario.get,reverse=True):
    print(k+":",dicionario[k])




