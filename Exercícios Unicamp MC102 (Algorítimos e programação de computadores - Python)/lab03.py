###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - BikeMax
# Nome: Guilherme Henrique Ichiro Seto Ito
# RA: 238706
###################################################

# Leitura de dados
sexo = input()
peso = float(input())
altura = int(input())
if sexo == "M" and peso<=70 and altura<=165:
    print("LX-39")
elif sexo == "M" and peso<=80 and altura>165 and altura<=190:
    print("BW-02")
elif sexo == "M" and peso<=100 and altura>190:
    print("MM-107")
elif sexo =="M" and peso>80 and peso<=100 and altura<=190 and altura>165:
    print("MM-107")
elif sexo == "M" and peso>70 and peso<=100 and altura<=165:
    print("LX-40")
elif sexo == "M" and peso>100 and altura<190 and altura>=150:
    print("CX-102")
elif sexo == "F" and altura<=140:
    print("LX-38")
elif sexo == "F" and peso<=90 and altura<=155 and altura>140:
    print("BW-03")
elif sexo == "F" and peso<=70 and altura<=170 and altura>155:
    print("BW-03")
elif sexo == "F" and peso<=90 and altura>170:
    print("BW-02")
elif sexo == "F" and peso>90 and altura>170:
    print("CX-102")
elif sexo == "F" and peso<=90 and altura<=170 and altura>155:
    print("CX-101")
elif sexo == "F" and peso>90 and altura<=170 and altura>140:
    print("CX-101")





# Seleção do modelo recomendado
