Q, classe, ordem = input().split()
Q = int(Q)
pokedex =[]

for _ in range(Q):
    cl, ord = input().split()
    pokedex.append({"C": cl,
             "O": int(ord)})

if classe == "N" and ordem == "D" :
        for inicio in range(1, Q):
           i = inicio
           while i >= 1 and \
           (pokedex[i]["C"] > pokedex[i-1]["C"] or 
            (pokedex[i]["C"] == pokedex[i-1]["C"] and
             pokedex[i]["O"] < pokedex[i-1]["O"])):
               
            pokedex[i], pokedex[i-1] = pokedex[i-1], pokedex[i]
            i -= 1    
        for _ in pokedex:
            print(_["C"], _["O"])
            
if classe == "L" and ordem == "D" :
        for inicio in range(1, Q):
           i = inicio
           while i >= 1 and \
           (pokedex[i]["O"] > pokedex[i-1]["O"] or 
            (pokedex[i]["O"] == pokedex[i-1]["O"] and
             pokedex[i]["C"] < pokedex[i-1]["C"])):
               
            pokedex[i], pokedex[i-1] = pokedex[i-1], pokedex[i]
            i -= 1 
        for _ in pokedex:
            print(_["C"], _["O"])               
 # ordem crescente   
if classe == "N" and ordem == "C" :
        for inicio in range(1, Q):
           i = inicio
           while i >= 1 and \
           (pokedex[i]["C"] < pokedex[i-1]["C"] or 
            (pokedex[i]["C"] == pokedex[i-1]["C"] and
             pokedex[i]["O"] < pokedex[i-1]["O"])):
               
            pokedex[i], pokedex[i-1] = pokedex[i-1], pokedex[i]
            i -= 1    
        for _ in pokedex:
            print(_["C"], _["O"])
                
if classe == "L" and ordem == "C" :
        for inicio in range(1, Q):
           i = inicio
           while i >= 1 and \
           (pokedex[i]["O"] < pokedex[i-1]["O"] or 
            (pokedex[i]["O"] == pokedex[i-1]["O"] and
             pokedex[i]["C"] < pokedex[i-1]["C"])):
               
            pokedex[i], pokedex[i-1] = pokedex[i-1], pokedex[i]
            i -= 1    
        for _ in pokedex:
            print(_["C"], _["O"])