n = int(input())
n1 = [int(n) for n in input().split()]
c = int(input())
e=0
for _ in range(n):
    if n1[_] == c:
        e = c
    else:
         continue   
if e == c:
    print(c)
else:
    print(-1)    