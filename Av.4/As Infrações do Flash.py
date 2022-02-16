n, m =[int(n) for n in input().split()]
l = [int(n) for n in input().split()]
c = 0

while c in l:
    l.remove(c)
cont = l[::-1]
cont = cont[0:m]
cont.reverse()
print(*cont)