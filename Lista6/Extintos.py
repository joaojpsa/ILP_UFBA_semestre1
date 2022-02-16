N =  int(input())
animais = []

for _ in range(N):
    n = input()
    animais.append(n)    

Q = int(input())

for v in range(Q):
    verifica = input()
    left = 0
    right = N - 1

    while left <= right:
        meio = (left+right)//2
        if animais[meio] == verifica:
            break
        elif verifica < animais[meio]:
            right = meio - 1
        else:
            left = meio + 1
    
    if animais[meio] == verifica:
        print(animais[meio], "vive!")
    else:
        print(verifica, "foi extinto :(")    