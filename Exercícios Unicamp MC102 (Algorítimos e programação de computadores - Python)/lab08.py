###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
# Nome: Guilherme Henrique Ichiro Seto Ito
# RA: 238706
###################################################

# DICA: use os métodos lower, replace, split e index
L = int(input())
pontuacao = [".", ",", ":", ";", "!", "?"]
frases = []
palindromos =[]
dicionario={}
k=0
for i in range (L):
    frases.append(str(input())) #transformou em lista as frases
    palavras = " ".join(frases) #juntou em uma string a lista
    palavras = palavras.lower() #deixou tudo minusculo
for p in pontuacao:
    palavras = palavras.replace(p," ") #tirou as pontuações
lp = palavras.split() #transformou as palavras em uma lista
for j in range (len(lp)):
    check=lp[j]
    if check == check[::-1]:
        palindromos.append(check) #lista de palindromos
for l in range (len(palindromos)): #transformando em dicionario
    palindro = palindromos[l]
    if not palindro in dicionario:
        dicionario[palindro] = 1
    else:
        dicionario[palindro] +=1
for (palindromo,quantidade) in dicionario.items():
    print(palindromo,quantidade)







