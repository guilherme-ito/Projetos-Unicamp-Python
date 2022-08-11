# Leitura no número de candidatos
n = int(input())
nomes = []
# Leitura do nome dos candidatos
for i in range(n):
    nomes.append(str(input()))

# Leitura dos votos
votos = []
for j in range(n + 2):
    votos.append(int(input()))
    total_votos = sum(votos)

# Votos válidos
votos_validos = votos[0:n]
total_votos_validos = sum(votos_validos)

# Se houve vencedor em primeiro turno
if max(votos_validos) > total_votos_validos / 2:
    x = max(votos_validos)
    posicao = votos_validos.index(x)
    vencedor = nomes[posicao]
    print(vencedor, "foi o vencedor da eleição")

# Se é necessário segundo turno
elif max(votos_validos) <= total_votos_validos / 2:
    y = max(votos_validos)
    posicao = votos_validos.index(y)
    primeiro = nomes[posicao]
    votos_validos.remove(y)
    z = max(votos_validos)
    votos_validos.insert(posicao,y)
    p = votos_validos.index(z)
    segundo = nomes[p]

    print("Haverá segundo turno entre:")
    print(primeiro)
    print(segundo)

print("Total de votos:", total_votos)
print("Votos válidos:", total_votos_validos)
