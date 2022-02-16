N = int(input())
S = int(input())
matrix= [[0] * 4 for l in range(4)]
cont = 0        
for _ in range(S):
    X, Y, V = map(int, input().split())
    matrix[X-1][Y-1] = V
for j in range(4):
    for l in range(4):
        cont += 1
        if matrix[j][l] == 0:
            matrix[j][l] = N*cont

                
    print(matrix)    
    