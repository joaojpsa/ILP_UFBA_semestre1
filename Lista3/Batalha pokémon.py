e, p = input().split()
e = int(e)
p = int(p)
c = 0

while e > 0 and p > 0:
    e -= p
    p -= 1
    c += 1

if e > p:
    print('F')
else:
    print(c)
