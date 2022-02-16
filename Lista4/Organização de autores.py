N = int(input())
f = [0]
g = []
for _ in range(N):
    n = input()
    n = n.title().split()
    f = n[-1:]
    
    for i in range(len(n) -1):
        s = n[i] 
               
        list(s)
        g.append(s[0])
        g.append(".")
        g.append(" ")
    g.append(f[0])   
    print("".join(g))
    g = []