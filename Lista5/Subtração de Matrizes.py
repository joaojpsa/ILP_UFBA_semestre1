N, M = map(int, input().split())
A = []
B = []


for i in range(N):
    n = [int(x) for x in input().split()]
    A.append(n)      
for i in range(N):
    n = [int(x) for x in input().split()]
    B.append(n)   
for _ in range(N):
    C = []
    for j in range(M):
       
        C.append(A[_][j] - B[_][j])
       
    print(*C)
    