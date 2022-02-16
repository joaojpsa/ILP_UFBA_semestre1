N = int(input())
mili =list( map(int, input().split()))

n = len(mili)

for _ in range (1, n):
    k = _
    while k >=1 and mili[k] < mili[k-1]:
        mili[k], mili[k-1] = mili[k-1], mili[k]
        k -= 1
 
meio = (len(mili)//2) 
print(mili[meio])
      

    