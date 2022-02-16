N = int(input())
matriz = []
h = 0
r = 0
c = 0
for _ in range(N):
    n = [int(x) for x in input().split()]
    matriz.append(n)
    
X, Y = map(int, input().split())
if X > Y:
    for i in matriz[X]:
        h += i
        matriz[X][c] = 0
        c+=1
    for j in range(N):
        r += matriz[j][Y]
        
elif Y >= X:    
    for j in range(N):
        r += matriz[j][Y]
        matriz[j][Y] = 0
        
    for i in matriz[X]:
        h += i
    
print("Harry", h)
print("Ron", r)
