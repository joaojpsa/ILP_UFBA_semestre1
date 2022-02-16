s = input()
q, p = input().split()
q = int(q)
s = s.replace(" ", "")

if s.count(p) == q:
    print(s.count(p))
    print("SIM!")
else:
    print(s.count(p))
    print("NAO!")    
    