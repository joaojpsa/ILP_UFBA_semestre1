
dim = []
coord = []
soma = 0
N = int(input())
for _ in range(N):
    n = [int(x) for x in input().split()]
    dim.append(n)

C = int(input())
for i in range(C):
    l, c = map(int, input().split())
    
    for j in range(1):
           soma += dim[l][c] 
     
print(soma)     