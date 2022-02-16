N, M = map(int, input().split())
dimen = list()
cont = 0
l = 0
c = 0
d = 0

for _ in range(N):
    n = list(map(int, input().split()))
    dimen.append(n)
   
for i in range(M):
    l, c = map(int, input().split())
    
    for j in range(l - 1, -1, -1):
        if dimen[j][c] == 1:
            
            d += 1
            dimen[j][c] = 0
            break
    
              
print(d)