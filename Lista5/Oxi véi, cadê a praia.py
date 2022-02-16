ilha = []

for _ in range(10):
    praias = input().split()
    ilha.append(praias)

for i in range(10):
    for j in range(10):
                    
        if i+1 <10:        
                if ilha[i+1][j] == "t" and ilha[i][j] == "*":
                    ilha[i+1][j] = "p" 
                if ilha[i][j] == "t" and ilha[i+1][j] == "*":
                    ilha[i][j] = "p"                              
        if j+1 < 10:
                if ilha[i][j+1] == "t" and ilha[i][j] == "*" :
                    ilha[i][j+1] = "p" 
                if ilha[i][j] == "t" and ilha[i][j+1] == "*":
                    ilha[i][j] = "p"                    
           
    print(*ilha[i])