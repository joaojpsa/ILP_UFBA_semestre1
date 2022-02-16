n = int(input())
si = [int(n) for n in input().split()]
sp = 0
c = 0
c1 = 0

for _ in range (n):
    sp += si[_]
    div = sp//2  
    
for i in range(len(si)):
    if c < div:
        c += si[i]
        c1 = i+1
    else:
        break    
print(c1)        
    