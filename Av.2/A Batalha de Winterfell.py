#Entrada
#A entrada consiste de duas linhas. Na primeira, serão dados 4 inteiros ‘dr’ (1 <= ‘dr’
#<= 2), ‘gu’, ‘ar’ e ‘dt’ (1 <= ‘gu’, ‘ar’, ‘dt’ <= 30000) que representam, respectivamente, o
#número de dragões, guerreiros, arqueiros e dothrakis. E na segunda linha será dado o
#número de caminhantes brancos ‘cb’ (1 <= ‘cb’ <= 2000000).
#Saída
#A saída consiste em uma única linha contendo ‘VITORIA’, se, de acordo com suas
#estimativas, eles vão ganhar a batalha, e ‘DERROTA’ se eles forem perder. Caso o
#exército de Jon Snow e Daenerys tenha a mesma força de combate que os
#Caminhantes Brancos, a humanidade ainda assim vencerá.


n, q = input().split()
n = int(n)
q = int(q)

sub = (q - n)%2

if n <= q and sub ==0:
    print('vendido')
else:
    print('sinto muito')