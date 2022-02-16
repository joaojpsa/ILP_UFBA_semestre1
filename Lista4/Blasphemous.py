n = int(input())
x = [int(n) for n in input().split()]
m = int(input())
c = m

for _ in x:    
    if _ != 1:
        m -= _
    elif _ == 1 and m > 0:
        m = c
    elif m < 0 :
        break   
if m > 0:
    print("Yes, you can") 
else:
    print("You Died")          