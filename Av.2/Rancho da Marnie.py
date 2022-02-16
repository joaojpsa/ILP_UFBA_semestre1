#Entrada
#A primeira linha contém um inteiro ‘N’ (1 <= N <= 103
#)
#representando a quantidade de feno que determinado aldeão quer comprar.
#A próxima linha contém um inteiro ‘Q’ (1 <= ‘Q’ <= 106
#) que é a
#quantidade de feno disponível para compra.
#Saída
#Você deverá imprimir se é possível vender o feno imprimindo
#“vendido” ou em caso contrário, imprimindo “sinto muito”.

n, q = input().split()
n = int(n)
q = int(q)

sub = (q - n)%2

if n <= q and sub ==0:
    print('vendido')
else:
    print('sinto muito')