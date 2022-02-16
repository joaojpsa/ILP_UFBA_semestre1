c = int(input())
countLM = 0
countT = 0
for _ in range(c):
    l, m, t = map(int, input().split())
    countLM += (l*m)
    countT += t
print(countLM + countT)    