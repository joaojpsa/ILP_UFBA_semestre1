N, M = map(int, input().split())
caminho = []

for _ in range(N):
    n = [int(x) for x in input().split()]
    caminho.append(n)

O = 0 
for l in range(N):
    if l == 0 or l%2 == 0:
        for i in range(M):
            O += caminho[l][i]
            if O < 0:
                O = 0
                
    elif l%2 != 0:
        for e in range(M-1, -1, -1):
            O += caminho[l][e] 
            if O < 0:
                O = 0          
print(O)            