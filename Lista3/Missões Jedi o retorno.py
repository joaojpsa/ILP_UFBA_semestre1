n, x, xpmin = input().split()
n = int(n)
x = int(x)
xpmin = int(xpmin)
c = 0
while c < n:
    xp, q = input().split()
    xp = int(xp) 
    q = int(q)
    c += 1
    if xpmin <= xp:
        xp += x
        q += 1
        print(xp, q)
    else:
        print(xp,q)    
