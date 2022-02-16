#s,n = map(int, input().split())

#pisa = [0]*10
#c = 0
#for _ in range(s):
#   p = int(input())
#    print(pisa)
#    for i in range(0, n, p):
#        print(i, n, p)
#        
#        pisa [i] = 1
#        print(pisa) 
#print(*pisa) 
s,n = map(int, input().split())
pisa = [0]*n

for _ in range(s):
    p = int(input())
       
    for i in range(0, n, p):     
        pisa [i] = 1
print(*pisa) 