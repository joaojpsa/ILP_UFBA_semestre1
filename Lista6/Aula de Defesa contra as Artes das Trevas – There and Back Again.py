N = int(input())
geral = list(map(str, input().split()))

M = int(input())
proibido = list(map(str, input().split()))

C = int(input())
c = list(map(str, input().split()))


for _ in range(C):
  
    esq = 0
    dir = N - 1
    
    while esq <= dir:
        
        meio = (esq + dir) // 2
        if geral[meio] == c[_]:
            break
        elif c[_] < geral[meio]:
            dir = meio - 1
        elif c[_]>geral[meio]:
            esq = meio + 1
            
    if geral[meio] == c[_]:
        print("Geral")
    else:
        print("Proibido")    


