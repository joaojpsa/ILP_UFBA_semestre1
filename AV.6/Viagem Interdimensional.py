N, M = map(int, input().split())

dimensoes = 0

n = list(map(int, input().split()))
m = list(map(int, input().split()))


for _ in range (M):
    
    esq = 0
    dir = N - 1
    
    while esq <= dir:
        
        meio = (esq + dir) // 2
        if n[meio] == m[_]:
            break
        elif m[_] < n[meio]:
            dir = meio - 1
        elif m[_]>n[meio]:
            esq = meio + 1
            
    if n[meio] == m[_]:
        dimensoes += 1

print(dimensoes)
