t = int(input())
c = 0
p = 100000
while p != 0:
    p = int(input())
    if p > t:
        c = p

if c > t:
    print('ALARME')
else:   
    print('O Havai pode dormir tranquilo')    
    
