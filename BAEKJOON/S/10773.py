N = int(input())
l = list()

for i in range(N):
    n = int(input())
    if n == 0:
        l.pop()
    else:
        l.append(n)

print(sum(l))