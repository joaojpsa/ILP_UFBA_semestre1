n = int(input())
x = [int(n) for n in input().split()]
p = int(input())
c = 0
for _ in range(len(x)):
    if x[_] <= p:

        c += x[_]
if c%2 == 0:
    print("tutturu")
else:
    print("SERN")    