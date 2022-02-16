n = int(input())
h = 0
m = 0
for _ in range(n):
    s = int(input())
    if s == 1:
        h += 1
    elif s == 2:
        m += 1
print(h)
print(m)            
