#n = int(input())
#xi = [int(x) for x in input().split()]
#
#for _ in range(0, n):
#    menor = _
#
#    for i in range (_ + 1, n):
#        if xi[menor] > xi[i] :
#            aux = xi[menor]
#            xi[menor] = xi[i]
#            xi[i] = aux
#
#print(*xi)

n = int(input())
c = [0]*1000001

xi = map(int, input().split())

for i in xi:
    c[i] += 1
for j in range (0, len(c)):
    cc = c[j]
    if cc != 0:
        print(j, end = " ")