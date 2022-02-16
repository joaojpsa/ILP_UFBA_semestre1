P = int(input())
homem = []
mulher = []
for _ in range(2):
    if _ == 0:
        I = list(map(int, input().split()))
        for fim in range(P - 1, 0, -1):
        
          
            imaior = 0
            for i in range(1, fim + 1):
                if I[i] < I[imaior]:
                    imaior = i
            I[imaior], I[fim] = I[fim], I[imaior]
            homem.append(I)
            
    elif _ ==1:
        I = list(map(int, input().split()))
        for fim in range(P - 1, 0, -1):
            
            imaior = 0      
            for i in range(1, fim + 1):
                if I[i] > I[imaior]:
                    imaior = i
            I[imaior], I[fim] = I[fim], I[imaior]
            mulher.append(I)
            
for p in range(P):
    print(homem[0][p], mulher[0][p])