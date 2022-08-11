###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Noite de Sono
# Nome: Guilherme Henrique Ichiro Seto Ito      
# RA: 238706
###################################################

# Leitura de dados#
   
h_1 = input( )
h_1 = int(h_1)
m_1 = input( )
m_1 = int(m_1)
h_2 = input( )
h_2 = int(h_2)
m_2 = input( )
m_2 = int(m_2)


# Cálculo do tempo dormido
if h_1>h_2 and (((h_2+24)*60+m_2)-((h_1*60)+m_1))>=480:
    print('True')
elif h_1<h_2 and (((h_2*60)+m_2)-((h_1*60)+m_1))>=480:
    print('True')
elif h_1 == h_2:
    print('False')
else:
    print('False')


# Impressão da resposta

