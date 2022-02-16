n, m = input().split()
n = int(n)
m = int(m)
c = 0
c_p = 0

for co in range (n):
    m = input().split()
    for co in m:
        co = int(co)
        c_p += co
        if c < c_p:
            c = c_p
        else:
            c = c    
    c_p -= c_p
print(c)