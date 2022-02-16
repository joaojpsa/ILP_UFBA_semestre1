N = int(input())
tabela = []

for _ in range(N):
    iplaneta, urgencia = input().split()
    tabela.append({"planeta": int(iplaneta),
             "urge": int(urgencia)})

for inicio in range(1, N):
       i = inicio
       while i >= 1 and \
           (tabela[i]["urge"] > tabela[i-1]["urge"] or 
            (tabela[i]["urge"] == tabela[i-1]["urge"] and
             tabela[i]["planeta"] < tabela[i-1]["planeta"])):
               
            tabela[i], tabela[i-1] = tabela[i-1], tabela[i]
            i -= 1
for aluno in tabela:
   print(aluno["planeta"], aluno["urge"])