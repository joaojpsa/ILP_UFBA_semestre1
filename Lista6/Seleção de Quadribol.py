N = int(input())
T = list(map(int, input().split()))

for _ in range(N):
    menor = _
    for i in range(_ + 1, N):
        if T[i] < T[menor]:
            menor =i
    T[_], T[menor] = T[menor], T[_] 


print(*T[0:8])