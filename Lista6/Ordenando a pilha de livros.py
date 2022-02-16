N = int(input())
livro = []
ordem = []
for _ in range(N):
    n = input()
    livro.append(n)

for fim in range(N - 1, 0, -1):
            
          
            imaior = 0
            for i in range(1, fim + 1):
                if livro[i] > livro[imaior]:
                    imaior = i
            livro[imaior], livro[fim] = livro[fim], livro[imaior]
for p in range(N):
    print(*livro[p])