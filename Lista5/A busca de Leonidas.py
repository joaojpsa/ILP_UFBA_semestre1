P = int(input())
p = 0
matriz =[]

for _ in range(10):
    X =[int(x) for x in input().split()]

    matriz.append(X)
    
    for i in range(10):
        if matriz[_][i] == P:
            p = P
         
        
if p == P:
    print("sim")
else:
    print("nao")         